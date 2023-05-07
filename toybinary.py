#python3.11.2
#imports
import math

#FIXME due to the bug in the init, a lot of other stuff might be wrong
#TODO make sure all functions support expos (2**expos indexing)
#TODO rename all self.count to self.count1 and make self.count0
#TODO add internal object names

class bitBox:
    """
    Bits for integers.
    """
    def __init__(self,integer,size=0):
        self.num=integer
        self.count=0 #TODO add counter of 1s in the number
        numberBin=bin(integer)
        self.bits=[0]*max(size,len(numberBin)-2)
        for i in range(0,len(numberBin)-2):
            self.bits[-i-1]=int(numberBin[-i-1])
            if self.bits[-i-1]==1:
                self.count+=1

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


    def __len__(self): #TODO it actually works with len(self) so I can replace all lens(self.bits)
        return len(self.bits)

    def flipBit(self,index=None,expos=None): #TODO just recalculate expos into index
        """Flips a bit, returns the new value

        expos is the inverse of index and points to the bit coresponding to 2**expos
        not input validation

        if index: flip index
            return new value
        if expos: flip expos
            return new value
        if both: flip slice ([4:7] is [4,6] interval notation)
            return (1 to 0, 0 to 1)
        if neither: flip all
            return (1 to 0, 0 to 1)
        """
        #both FIXME num is not calculated
        if index!=None and expos!=None:
            count0=0
            count1=0
            for i in range(index,expos):
                if self.bits[i]:
                    count0+=1
                    self.num-=2**(len(self)-index-1)
                    self.bits[i]=0
                else:
                    count1+=0
                    self.bits[i]=1
                    self.num+=2**(len(self)-index-1)
            return (count0,count1)
        #neither
        elif index==None and expos==None:
            count0=0
            count1=0
            for i in range(len(self.bits)):
                if self.bits[i]:
                    count0+=1
                    self.bits[i]=0
                else:
                    count1+=1
                    self.bits[i]=1
            self.num=2**len(self)-self.num
            return (count0,count1)
        #either
        elif expos==None:
            expos=len(self.bits)-index-1
        elif index==None:
            index=len(self.bits)-expos-1
        if self.bits[index]:
            self.bits[index]=0
            self.num-=2**(expos)
        else:   
            self.bits[index]=1
            self.num+=2**(expos)
        return self.bits[index]

    def calibrate(self):
        """
        Recalculates and returns the value of the bitPile number.
        """
        self.num=0
        self.count=0
        for i in range(len(self.bits)):
            if self.bits[i]:
                self.num+=2**(len(self.bits)-i-1)
                self.count+=1
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

    def add(self,value=1,bitObject=None): #TODO add bitobject addition
        for plus1 in range(value): #TODO there has to be a better way
            buffer=1
            self.num+=1
            for b in range(len(self.bits)-1,-1,-1):
                if self.bits[b]+buffer==2:
                    self.bits[b]=0
                    buffer=1
                elif self.bits[b]+buffer==0:
                    break
                else:
                    self.bits[b]=1
                    buffer=0
        return self.num
        
    def subtract(self,value):
        for minus1 in range(value): #TODO there has to be a better way
            self.num-=1
            for b in range(len(self.bits)-1,-1,-1):
                if self.bits[b]==1:
                    self.bits[b]=0
                    break
                else:
                    self.bits[b]=1
        return self.num

    def nextPermutation(self): #TODO add number calculation
        counter=0
        for b in range(len(self.bits)-1,-1,-1):
            if b==0:
                self.flipBit(len(self)-self.count,len(self))
                if self.count==len(self):
                    self.count=0
                else:
                    self.count+=1
                    self.flipBit(0,self.count)
                break
            if self.bits[b]==1:
                counter+=1
            elif self.bits[b]==0 and self.bits[b-1]==1:
                self.bits[b]=1
                self.bits[b-1]=0
                self.flipBit(len(self)-counter,len(self))
                self.flipBit(b+1,b+counter+1)
                break
        return self.count


        

"""
Bits for floats and other suffesticated math
"""
class bitBin:
    pass

"""
Load of bits
"""
class bitShelf:
    def __init__(self):
        self.bits=[]
        self.count=0

    def printBits(self):
        print("Binary Length:",len(self.bits),"\nBinary: ",end="")
        for bit in self.bits:
            print(bit,end="")
        print()
    
    def fromString(self,string):
        for c in string:
            self.bits.extend(numToBits(ord(c),8))
        return len(self)

    def toString(self):
        output=""
        for i in range(0,len(self.bits),8):
            output+=chr(calc_num(self.bits[i:i+8]))
        return output

    def __getitem__(self,index):
        """
        returns bitvalue at a given index, changing might break num. 
        Use setbit(index, value) instead.
        Slices also work: self.bits[4:9]
        """
        if type(index)==tuple:
            return self.bits[index[0]:index[1]]
        return self.bits[index]


    def __len__(self): #TODO it actually works with len(self) so I can replace all lens(self.bits) everywhere else (not here)
        return len(self.bits)
    

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