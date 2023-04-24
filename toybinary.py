#python3.11.2
#imports
import math

#FIXME due to the bug in the init, a lot of other stuff might be wrong
#TODO make sure all functions support expos (2**expos indexing)
#TODO remove self.length, it's useless
class bitPile:
    """
    Bits for integers.
    """
    def __init__(self,integer,size=0):
        self.num=integer
        numberBin=bin(integer)
        self.bits=[0]*max(size,len(numberBin)-2)
        for i in range(0,len(numberBin)-2):
            self.bits[-i-1]=int(numberBin[-i-1])
        self.length=len(self.bits)

    def printBits(self):
        print("Number:",self.num)
        print("Binary Length:",self.length,"\nBinary: ",end="")
        for bit in self.bits:
            print(bit,end="")
        print()
    
    def __getitem__(self,index):
        """
        returns bitvalue at a given index, changing might break num. 
        Use setbit(index, value) instead.
        Slices also work: self.bits[4:9]
        """
        if type(index)==tuple:
            return self.bits[index[0]:index[1]]
        return self.bits[index]


    def __len__(self):
        return self.length

    def flipBit(self,index=None,expos=None): #TODO add pos based on input like 2,4,8
        """
        Flips a bit, returns the new value
        expos is the inverse of index and points to the bit corersponding to 2**expos

        if index: treat index
        if expos: treat expos
        if both: treat slice
        if neither: flip all
        """ #FIXME fix all of this
        if index==None:
            if expos!=None:
                if self.bits[self.length-expos-1]:
                    self.bits[self.length-expos-1]=0
                    self.num-=2**expos
                else:   
                    self.bits[self.length-expos-1]=1
                    self.num+=2**expos
                return self.bits[self.length-expos-1]
        elif expos==None:
            if self.bits[index]:
                self.bits[index]=0
                self.num-=2**(self.length-index-1)
            else:   
                self.bits[index]=1
                self.num+=2**(self.length-index-1)
            return self.bits[index]

    def calibrate(self):
        """
        Recalculates and returns the value of the bitPile number.
        """
        self.num=0
        self.length=len(self.bits)
        for i,bit in enumerate(self.bits):
            if bit:
                self.num+=2**(self.length-i-1)
        return self.num

    def setbit(self,index,value): #TODO add pos based on input like 2,4,8
        """
        Sets a bit to a given value.
        returns past value
        """
        if self.bits[index]==value:
            return value
        elif value: #1
            self.bits[index]=value
            self.num+=2**(self.length-index-1)
            return 0
        else: #0
            self.bits[index]=value
            self.num-=2**(self.length-index-1)
            return 1

    def resize(self,left,right):
        """
        forcefully resizes the list
        right and left can ne negative accordingly
        there is no protection
        returns new list length
        """
        if left>0:
            self.bits[:0]=[0]*left
        if right>0:
            self.bits.extend([0]*right)
        if left<0:
            del self.bits[:left]
        if right<0:
            del self.bits[right+1:]
        
        self.length=len(self.bits)

    def append(self,value):
        """
        append a bit at the end #TODO remake this into insert
        """
        self.bits.append(value)
        self.num=self.num*2+value
        self.length+=1
        

"""
Bits for floats.
"""
class bitFinePile:
    pass

"""
Load of bits
"""
class bitMountain:
    pass

"""
bitlist to number
"""
def calc_num(bitlist,extendTo=0): #TODO add and an "Extend in front"
    #could have just multiplied by 2**(extendTo-len(bitlist)) at the end
    num=0
    extendTo=max(extendTo,len(bitlist))
    for bitI in range(len(bitlist)):
        if bitlist[bitI]:
            num+=2**(extendTo-bitI-1)
    return num

"""
number to bitlist
"""
def numToBits(number,size=0):
    numberBin=bin(number)
    bitlist=[0]*max(size,len(numberBin)-2)
    for i in range(0,len(numberBin)-2):
        bitlist[-i-1]=int(numberBin[-i-1])
    return bitlist

"""
Conversions of binary into a anb64 based on base64 but with extra features.
Encoding
Input: one of the toybinary datatypes
Output: anb64 string

Decoding:
Input: one of the toybinary datatypes
Output: anb64 string

standart: =0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz+ 
seperator: /
"""

anb64map="=0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz+"
def anb64encode(bitObject): #FIXME make it work with a bitlist
    output=""
    #calculate length #FIXME the 6-standdarization is a mess
    length=bin(bitObject.length)[2:]
    if len(length)%6>0:
        length="0"*(6-len(length)%6)+length
    for i in range(0,len(length),6):
        output+=anb64map[int(length[i:i+6],2)]
    output+="/"
    #main content
    for i in range(0,bitObject.length,6):
        output+=anb64map[calc_num(bitObject.bits[i:i+6],extendTo=6)]
    return output

"""
if outputtype bitObject, pass your own bitObject
"""
def anb64decode(string,outputType="bitlist",bitObject=None):
    #TODO make this more efficient, maybe add proper names
    bitlist=[]
    #figure out the length
    length=0
    seperator=string.find("/")
    for symbI in range(0,seperator):
        length=length*64+anb64map.find(string[symbI])
    #figure out everything
    for symbI in range(seperator+1,len(string)):
        bitlist.extend(numToBits(anb64map.find(string[symbI]),size=6))
    del bitlist[length:]
    #output
    if outputType=="bitlist":
        return bitlist
    elif outputType=="bitObject":
        bitObject.bits=bitlist
        bitObject.calibrate()
        return bitObject