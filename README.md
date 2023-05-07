# ToyBinary

I was so frustrated about python binary being so complicated, and that I couldn't play around with it, that I decided to make my own python library for exploring binary.
Obviously this library is really inefficient and is written in python, and should be used only for learning&trying around (that's why it is called toy). If you are planning on writting something that will actually be used, do yourself a favor and learn C. 

## Documentation

Toybinary has 3 custom datatypes (they will sometimes be refered to as bitObjects):

`toybinary.bitBox()` *~: work in progress*

`toybinary.bitBin()` *X: not ready yet*

`toybinary.bitShelf()` *X: not ready yet*

Base64 inspired anBase64 encoding: `anb64encode` and `anb64decode`

And 2 supporting functions: `calc_num` and `numToBits`

### bitBox

bitBox is designed for smaller numbers, I tested it with 128 bit number, but I am not sure how much more python can handle without issues. It's just a normal box of toys. 

```python
import toybinary #for now the import is manual from a nearby directory

myNum=toybinary.bitBox(1234,20) #myNum will be number 1234 stored in 20 bits
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

#now we want to resize the number of bits in the number
myNum.resize(-6,2) #remove 6 leading bits, and add 2 at the end
myNum.printBits()
#> Number: 4928
#> Binary Length: 16 
#> Binary: 0001001101000011
```

### bitBin

When I get to work on it, it will be similar to bitBox, but focused more towards dealing with floating point and negative. It is a messy bin of toys.

### bitShelf

When I get to it, it will be a raw sequence of bits without any kind of number or math. Designed for very large amount of bits (eg. a text file in binary). Unlike bitBoxes that are tied to numbers, the mountain is centered around strings, files and manipulation. It is a huge shelf with toys.

### anBase64

anBase64 is based on base64 encoding, but preserves length - so no additional data is added when usign it. This comes at the cost of 1 extra character at the end of the string.

anb64 encodings look like this: `BiNaRyDaTa%` where `%` a number of binarydata length mod 6 in plain text.
I made this decidion because someone decoding the string with a normal base 64 decoder will assume that the end was a bunch of giberish and will still be able to recreate the orginal data with minimal issues. When decoding ASCII, first 6 characters are techinical (NULL, EOT, etc.) and will probably be manually removed by the user.

Here are some examples:

`111011111100000101000100000011000000011000100100011101110010100` -> `78FEDAYkdyg3`

`1110110101111011111000111100100101111111010101011010000100100000` -> `7XvjyX9VoSA4`

`11001111111000100110101110010111100000100101101011110100011001111000010101101011` -> `z+Jrl4Ja9GeFaw2`

`1111111011010011` -> `/tM4`

`10011000111110011110010101100` -> `mPnlY5`

How to use encode and decode:

`toybinary.anb64encode(bitObject)` (such as bitBox/bitShelf etc)

`toybinary.anb64decode(string,outputType= "bitlist" or "bitObject", bitObject=yourBitObject)` 

string is the anb64 string, output is a bitlist ([0,1,0,0,1,0...etc.]) by defaoult but can be set to bitObject (bitBox/bitBin/bitShelf), in this case you will have to pass it an already existing object (or just pass it `toybinary.bitPile(0,0)`). I recomend using bitShelf if the encoding is very large.


## TODO
- Add consistent naming
