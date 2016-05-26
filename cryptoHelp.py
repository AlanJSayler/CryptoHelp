import math
alphabet = """ABCDEFGHIJKLMNOPQRSTUVWXYZ"""
#Take the letters and make them into the digits associated with their index in
#alphabet, return -1 on error
def letterToDigit(toTranslate):
    for i in range(0,len(alphabet)):
        if(toTranslate == alphabet[i]):
            return i
    return -1
#Euclid's algorithm to determine GCD of two positive integers. Returns
#The GCD. Returns -1 if they are not positive integers
def gcd(a,b):
    if not isPositiveInt(a) or not isPositiveInt(b):
        return -1
    while b != 0:
        temp = b
        b = a % temp
        a = temp
    return a

#determines if a number is a positive integer. Returns 0 if it is not
#and 1 if they are
def isPositiveInt(a): 
    if a % 1 != 0 or a < 1:
        return 0
    return 1

#Since the alphabet is limited to ASCII characters, it can never
#be that big, and hence, inverting a key will not take long by brute
#force. We could change this to Euclid's extended algorithm for a
#lower time complexity
def inverseInAlphabet(a):
    for i in range(0,len(alphabet)):
        if (a * i) % len(alphabet) == 1:
            return i
    return -1

def validateAffineKeys(coefKey,offKey):
    if coefKey == 1:
        print("Warning: A value of 1 as the coefficient key reduces" +
             " the affine cipher to being a Caesar shit")
    if isPositiveInt(offKey) != 1 or isPositiveInt(coefKey) != 1:
        print("Error: You need to choose positive integers for your keys")
        return -1
    if gcd(coefKey, len(alphabet)) != 1:
        print("Error: you need to choose positive integers for your keys")
        return -1
    return 1
#encrypt an affine cipher given an a,b key pair
def encryptAffine(coefKey, offKey, plainText):
    if validateAffineKeys(coefKey,offKey) != 1:
        return
    cipherText = ''
    for i in range(0,len(plainText)):
        if(letterToDigit(plainText[i]) == -1):
            print("Error: Cannot encrypt a letter not in the specified alphabet!")
            return
        cipherText += alphabet[(letterToDigit(plainText[i]) * coefKey + offKey) % len(alphabet)]
    return cipherText

#inverse function of an affine cipher given a,b key pair
def decryptAffine(coefKey, offKey, cipherText):
    if validateAffineKeys(coefKey,offKey) != 1:
        return
    plainText = ''
    for i in range(0,len(cipherText)):
        if(letterToDigit(cipherText[i]) == -1):
            print("Error: Cannot encrypt a letter not in the specified alphabet!")
            return
        plainText += alphabet[((letterToDigit(cipherText[i]) - offKey) * inverseInAlphabet(coefKey)) %len(alphabet)]
    return plainText

#take a^b mod c quickly using the doubling exponents trick
def raiseToMod(a,b,c):
    if(isPositiveInt(a) != 1 or isPositiveInt(b) != 1 or isPositiveInt(c) != 1):
        print("Error: We're assuming we're working in Z*, so a,b, and c need to" +
        " be positive integers to take a^b mod c")
    exp = 1
    curr = a
    #use doubling trick at first...
    while(exp <= b/2):
        curr = curr * curr
        curr = curr % c
        exp = exp * 2 
    while(exp < b):
        curr = curr*a
        curr = curr%c
        exp = exp + 1
    return curr %c

#use Fermat's little theorem to test if some integer is likely prime
#this does not guarantee primality. Return -1 if number is definitely not
#prime. Return 1 if number is likely prime
#TODO: generalize away from python's int type to allow for 'real' (i.e. huge)
#tests, rather than the 'toy' tests used for class
def isLikelyPrime(p):
    if(isPositiveInt(p) != 1):
        print("Error: Nonpositive or Noninteger numbers aren't prime for our purposes")
        return -1
    if p == 2:
        return 1
    if(raiseToMod(2,p,p) == 2):
        return 1
    return -1

#checks if a number is prime. Returns 1 iff the number is a positive
#,prime integer. This algorithm takes every prime <= the number in question
#and sees if it divides the number in question. This is the fastest algorithm
#that guarantees to return true iff the integer is prime
def isPrime(p):
    if(isPositiveInt(p) != 1):
        print("Error: Nonpositive or Noninteger numbers aren't prime for our purposes")
        return -1
    if(p == 1):
        print("1 is obviously the unit")
        return -1
    if(p == 2):
        return 1
    curr = 2
    while curr <= math.sqrt(p):
        if(isPrime(curr) == 1):
            if p % curr == 0:
                return -1
        curr = curr + 1
    return 1

#find the inverse of a mod n, -1 on error. Since we're doing
#'toy' problems, do this with bruth force rather than
#Euclid's extended algorithm
def multiplicativeInverseMod(a,n):
    if (isPositiveInt(a) != 1 or isPositiveInt(n) != 1):
        print("Error: Need Positive Integers")
        return -1
    for i in range(1,n):
        if ((a * i % n) == 1):
            return i
    return -1
