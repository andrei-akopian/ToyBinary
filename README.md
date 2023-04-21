# ToyBinary

I was so frustrated about python binary being so complicated, and that I couldn't play around with it, that I decided to make my own python library for exploring binary.
Obviously this library is really inefficient and is written in python, and should be used only for learning&trying around (that's why it is called toy). If you are planning on writting something that will actually be used, do yourself a favor and learn C. 

## Documentation

Toybinary has 3 custom datatypes:

`toybinary.bitPile()` *~: work in progress*

`toybinary.bitFinePile()` *X: not ready yet*

`toybinary.bitMountain()` *X: not ready yet*

Base64 inspired anBase64 encoding: `anb64encode` and `anb64decode`

And 2 supporting functions: `calc_num` and `numToBits`

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
print(myNum.calibrate()) #will recompute the base 10 value of the bits
myNum.printBits()
#> Number: 34000 <# it went from 34002 to 34000, the 2 got removed as it was second to last
#> Binary Length: 20 
#> Binary: 00001000010011010000
```

### BitFinePile

When I get to work on it, it will be similar to BitPile, but focused more towards dealing with floating point and negative.

### bitMountain

When I get to it, it will be a raw sequence of bits without any kind of number or math. Designed for very large amount of bits (eg. a text file in binary). Unlike bitPiles that are tied to numbers, the mountain is centered around strings, files and conversions.

### anBase64

anBase64 encoding format is inspired by base64, but doesn't loose any information, thus is able to store binary of some unknown length. It is also designed to store additional metadata.

anb64 uses this table: `=0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz+`
Each symbol represents the 6bit sequence of its index.

There is also an aditional special symbol: `/`
It acts as a seperator for metadata.

anb64 encodings look like this: `LeNgTh/BiNaRyDaTa`

First the length is encoded normally as a number. eg. if the length is `63 (111111)` then it will become `+/` since + has the 63rd index which corresponds to `111111`

Then the binary is decoded normally with potential zeros at the end.

Here are some examples:

`101011000000110001100100` -> `N/g=mZ`

`110000110011110101110001101010110101010110010111010110100100101100010101001011010001` -> `0J/loqmfqLMLZhKAG`

`1010010101010101001100110011111010101110100011010001010001001110` -> `0=/eKJoEfvC43t`

`10000010110010110100111100100010111110010001` -> `h/VhiE7kZF`

`1000101010100000101100111100101111000110000110000010100000000011011000111011010111010111100000111001110111111010100010` -> `0r/Xf1onxNN9=CYiST2cUf7`

How to use encode and decode:

`toybinary.anb64encode(bitObject)` (such as bitPile/bitMountain etc)

`toybinary.anb64decode(string,outputType= "bitlist" or "bitObject", bitObject=yourBitObject)` 

string is the anb64 string, output is a bitlist ([0,1,0,0,1,0...etc.]) by defaoult but can be set to bitObject (bitPile/bitFinePile/bitMountain), in this case you will have to pass it an already existing object (or just pass it `toybinary.bitPile(0,0)`). I recomend using bitMountain if the encoding is very large.
