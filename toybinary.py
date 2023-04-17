"""
Bits for integers.
"""
class bitPile:
    def __init__(self,integer):
        self.num=integer
        self.bits=[]
        for bit in bin(integer)[2:]:
            if bit=="1":
                self.bits.append(1)
            else:
                self.bits.append(0)
        self.length=len(self.bits)

    def printBits(self):
        print("Number:",self.num)
        print("Binary Length",self.length,"\nBinary: ",end="")
        for bit in self.bits:
            print(bit,end="")
        print()
    
    """
    returns bitvalue at a given index, changing might break num. 
    Use setbit(index, value) instead.
    """
    def __getitem__(self,index):
        return self.bits[index]


    def __len__(self):
        return self.length

    """
    Flips a bit, returns the new value
    """
    def flipBit(self,index=None,position=None): #TODO add pos based on input like 2,4,8
        if index is None:
            index=self.length-position-1
        if self.bits[index]:
            self.bits[index]=0
            self.num-=2**(self.length-index-1)
        else:
            self.bits[index]=1
            self.num+=2**(self.length-index-1)
        return self.bits[index]

    """
    Recalculates and returns the value of the bitPile number.
    """
    def calc_num(self):
        self.num=0
        for i,bit in enumerate(self.bits):
            if bit:
                self.num+=2**(self.length-i-1)
        return self.num

    """
    Sets a bit to a given value.
    returns past value
    """
    def setbit(self,index,value):
        if self.bits[index]==value:
            return value
        elif value: #1
            self.num+=2**index
            return 0
        else: #0
            self.num-=2**index
            return 1

    """
    forcefully resizes the number of bits
    anchor: 0 -left 1- right
    """
    def resize(self,newlength,anchor=0): #TODO add size increase
        if anchor==1:
            del self.bits[:self.length-newlength]
        elif anchor==0:
            del self.bits[newlength:]
        self.newlength
        

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