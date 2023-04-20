# ToyBinary

I was so frustrated about python binary being so complicated, and that I couldn't play around with it, that I decided to make my own python library for exploring binary.
Obviously this library is really inefficient and is written in python, and should be used only for learning&trying around (that's why it is called toy). If you are planning on writting something that will actually be used, do yourself a favor and learn C. 

## Documentation

Toybinary has 3 custom datatypes:

`toybinary.bitPile()` *~: work in progress*

`toybinary.bitFinePile()` *X: not ready yet*

`toybinary.bitMountain()` *X: not ready yet*

### BitPile

BitPile is designed for smaller numbers, I tested it with 128 bit number, but I am not sure how much more python can handle without issues.

```python
import toybinary #for now the import is manual

myNum=toybinary.bitPile(1234,20) #myNum will be number 1234 stored in 20 bits
myNum.flipBit(4) #flip the 4th bit

#now lets see the result my typing
myNum.printBits()
#> Number: 34002
#> Binary Length: 20 
#> Binary: 00001000010011010010
#              ^here we flipped a bit, the number also changed

myNum.setbit(18,0) #lets set 18th bit to 0
print(myNum[18]) #you can also index the bits

#but I don't recomend to modify bits through indexing, 
#beacuse the internal number value will break. You will have to use
print(myNum.calc_num()) #will recompute the base 10 value of the bits
myNum.printBits()
#> Number: 34000 <# it went from 34002 to 34000, the 2 got removed as it was second to last
#> Binary Length: 20 
#> Binary: 00001000010011010000
```

### BitFinePile

When I get to work on it, it will be similar to BitPile, but focused more towards dealing with floating point and negative.

### bitMountain

When I get to it, it will be a raw sequence of bits without any kind of number or math. Designed for very large amount of bits (eg. a text file in binary). Unlike bitPiles that are tied to numbers, the mountain is centered around strings, files and conversions. 
