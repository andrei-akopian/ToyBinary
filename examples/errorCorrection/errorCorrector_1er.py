import sys
sys.path.append('../../')

import toybinary
import random

## setupConstants ##
HASHSIZE=3
DATASIZE=4
# DATA=[0,0,0,0]
# ERRORPOS=0
ERRORPOS=random.randint(0, DATASIZE+HASHSIZE-1)
DATA=[random.randint(0,1) for x in range(DATASIZE)]

def corhash(data,HASHSIZE):
    chash=toybinary.bitBox(0,HASHSIZE)
    iterator=toybinary.bitBox(1,HASHSIZE)
    i=0
    while iterator.nextPermutation() > 0 and i < len(data):
        if data[i]:
            for j in range(len(iterator)):
                if iterator[j]:
                    chash.flipBit(j)
        i+=1
    return chash

def fixerror(data,erroredhash,HASHSIZE,DATASIZE):
    errorhashmap=[0]*HASHSIZE
    for i in range(HASHSIZE):
        if not(data[i]==erroredhash[i]):
            errorhashmap[i]=1
    print("--Error difference/key--")
    print(errorhashmap)
    print("--Error Size--")
    print(sum(errorhashmap))

    #error in hash
    if sum(errorhashmap)==1:
        print("-Hash Error, Data good")
        errorPos=errorhashmap.index(1)
        data.flipBit(errorPos)
        return errorPos
    #error in data
    else:
        print("-Error in Data")
        iterator=toybinary.bitBox(1,HASHSIZE)
        i=0
        while iterator.nextPermutation() > 0 and i < len(data):
            if iterator.bits==errorhashmap:
                print("--Error Spot--\n",i)
                data.flipBit(i+HASHSIZE)
                return i+HASHSIZE
            i+=1

#initial
print("==INITIAL==")
data=toybinary.bitBox(0,DATASIZE)
data.bits=DATA[:]
print("--Data--")
print(data.bits)

print("--Hash--")
correctionHash=corhash(data, HASHSIZE).bits
print(correctionHash)

print("--Final Data--")
data.bits=correctionHash+data.bits
print(data.bits)

#with Error
print("==ERROR==")
data.flipBit(ERRORPOS)

print("--Data with Error--")
print(data.bits)

print("--Hash with Error--")
erroredhash=corhash(data[HASHSIZE:], HASHSIZE).bits
print(erroredhash)

#correct
print("==FIX ERROR==")
fixerror(data,erroredhash,HASHSIZE,DATASIZE)

print("--Fixed Data--")
print(data.bits)

print("--Hash--")
fixedDataHash=corhash(data[HASHSIZE:], HASHSIZE).bits
print(fixedDataHash)

print("--Check--")
print("Data:",data[HASHSIZE:]==DATA)
print("Hash:",fixedDataHash==correctionHash)