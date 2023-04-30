#python3.11.2
#imports
import math

#FIXME due to the bug in the init, a lot of other stuff might be wrong
#TODO make sure all functions support expos (2**expos indexing)
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

    def printBits(self):
        print("Number:",self.num)
        print("Binary Length:",len(self.bits),"\nBinary: ",end="")
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
        return len(self.bits)

    def flipBit(self,index=None,expos=None): #TODO add pos based on input like 2,4,8
        """
        Flips a bit, returns the new value
        expos is the inverse of index and points to the bit corersponding to 2**expos

        if index: flip index
        if expos: flip expos
        if both: flip slice
        if neither: flip all
        """ #FIXME fix all of this
        if type(index)==int and type(expos)==int:
            for i in range(index,expos):
                if self.bits[i]:
                    self.bits[i]=0
                else:
                    self.bits[i]=1
        elif type(index)==int:
            if self.bits[index]:
                self.bits[index]=0
                self.num-=2**(len(self.bits)-index-1)
            else:   
                self.bits[index]=1
                self.num+=2**(len(self.bits)-index-1)
            return self.bits[index]
        elif type(expos)==int:
            if self.bits[len(self.bits)-expos-1]:
                self.bits[len(self.bits)-expos-1]=0
                self.num-=2**expos
            else:   
                self.bits[len(self.bits)-expos-1]=1
                self.num+=2**expos
            return self.bits[len(self.bits)-expos-1]
        else:
            for i in range(len(self.bits)):
                if self.bits[i]:
                    self.bits[i]=0
                else:
                    self.bits[i]=1

    def calibrate(self):
        """
        Recalculates and returns the value of the bitPile number.
        """
        self.num=0
        for i in range(len(self.bits)):
            if self.bits[i]:
                self.num+=2**(len(self.bits)-i-1)
            self.bits[i]=int(self.bits[i])
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
            self.num+=2**(len(self.bits)-index-1)
            return 0
        else: #0
            self.bits[index]=value
            self.num-=2**(len(self.bits)-index-1)
            return 1

    def resize(self,left,right,filler=0):
        """resizes the list

        right and left can ne negative accordingly
        filler is the type of bit (0 or 1) the extra spaces will be filled with
        there is no protection against cutting away to much etc.
        returns new list length

            bitPile.bits=[0,0,1,1,0]
            bitPile.resize(-2,2,1) #bitPile.bits => [1,1,0,1,1]
        """
        if left<0:
            self.num=self.num%(2**(len(self.bits)+left))
            del self.bits[:-left]
        if right<0:
            self.num=self.num//(2**right)
            del self.bits[-right+1:]
        if left>0:
            self.bits[:0]=[filler]*left
        if right>0:
            self.num=self.num*(2**right)
            self.bits.extend([filler]*right)
        return len(self.bits)

    def append(self,value):
        """
        append a bit at the end
        """
        self.bits.append(value)
        self.num=self.num*2+value

    def insert(self,index,value):
        """
        Typical instert function
        """
        self.bits.insert(index, value)
        #TODO the math for self.num is to complex, so I just use calibrate 
        self.calibrate()
        

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
def calc_num(bitlist,extendTo=0):
    '''calculates the base10 value of a sequence of bits

    nvip
    bitlist=list of booleans
    extendTo=pretends there were extra bits at the end

    just loops through, adds 2^postition to num
    '''
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

standard: =0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz+ 
"""

anb64map="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
def anb64encode(bitObject): #FIXME make it work with a bitlist
    output=""
    for i in range(0,len(bitObject.bits),6):
        output+=anb64map[calc_num(bitObject.bits[i:i+6],extendTo=6)]
    output+=str(len(bitObject.bits)%6)
    return output

"""
if outputtype bitObject, pass your own bitObject
"""
def anb64decode(string,outputType="bitlist",bitObject=None):
    #TODO make this more efficient, maybe add proper names
    bitlist=[]
    #figure out everything
    for symbI in range(len(string)-1):
        bitlist.extend(numToBits(anb64map.find(string[symbI]),size=6))
    lenMod=int(string[-1])
    if lenMod>0:
        del bitlist[lenMod-6:]
    #output
    if outputType=="bitlist":
        return bitlist
    elif outputType=="bitObject":
        bitObject.bits=bitlist
        bitObject.calibrate()
        return bitObject