import sys
sys.path.append('../../')

import toybinary

stringAsBits=toybinary.bitShelf()
stringAsBits.fromString(input("Enter:"))
stringAsBits.printBits()

h=toybinary.anb64encode(stringAsBits)
print(h)

backToString=toybinary.anb64decode(h,outputType="bitObject",bitObject=toybinary.bitShelf())
backToString.printBits()
print(backToString.toString())