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
#encrypt an affine cipher given an a,b key pair
def encryptAffine(coefKey, offKey, plainText):
    if coefKey == 1:
        print("Warning: A value of 1 as the coefficient keyi " +
              "reduces the affine cipher to being a Caesar shift")
    if isPositiveInt(offKey) != 1 or isPositiveInt(coefKey) != 1:
        print("Error: you need to choose positive integers for you keys") 
        return -1
    #Check if the coefficient key is coprime to the length of the Alphabet
    if gcd(coefKey, len(alphabet)) != 1:
        print("Error: you need to pick a coefficient key that is coprime" +
              " to the length of your alphabet")
        return -1
    cipherText = ''
    for i in range(0,len(plainText)):
        if(letterToDigit(plainText[i]) == -1):
            print("Error: Cannot encrypt a letter not in the specified alphabet!")
            return
        cipherText += alphabet[(letterToDigit(plainText[i]) * coefKey + offKey) % len(alphabet)]
    return cipherText
