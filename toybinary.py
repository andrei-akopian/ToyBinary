"""
Bits for integers.
"""
#FIXME due to the bug in the init, a lot of other stuff might be wrong
class bitPile:
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
    def flipBit(self,index): #TODO add pos based on input like 2,4,8
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
    def setbit(self,index,value): #TODO add pos based on input like 2,4,8
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

    """
    forcefully resizes the number of bits
    anchor: 0 -left 1- right
    """
    def resize(self,newlength,anchor=0): #TODO add size increase and change this one completely
        if anchor==1:
            del self.bits[:self.length-newlength]
        elif anchor==0:
            del self.bits[newlength:]
        self.length=newlength

    """
    append a bit at the end #TODO remake this into insert
    """
    def append(self,value):
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