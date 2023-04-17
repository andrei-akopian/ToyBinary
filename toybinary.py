"""
Bits for integers.
"""
class bitPile:
    def __init__(self,integer):
        self.num=integer
        self.bits=[]
        for bit in bin(integer)[:2]:
            self.bits.append(bit=="1")
        self.length=len(self.bits)

    def printBits(self):
        print("Number:",self.num)
        print(self.length,"bit's long")
        for bit in self.bits:
            print(bit,end="")
        print("\n")
    
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
    def flipBit(self,index):
        if self.bits[index]:
            self.bits[index]=0
            self.num-=2**index
        else:
            self.bits[index]=1
            self.num+=2**index
        return self.bits[index]

    """
    Recalculates and returns the value of the bitPile number.
    """
    def calc_num(self):
        self.num=0
        for i,bit in enumerate(self.bits):
            if bit:
                self.num+=2**i
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
Bits for floats.
"""
class bitFinePile:
    pass

"""
Load of bits
"""
class bitMountain:
    pass