from randWord import *


def encrypt(text):
    # This method :
    # Encrypts the text given in the param.
    # A 3 digit random key is retured by genrtNum()
    # and is stored in 'key'
    # then a list is created which stores random small
    # alphabets numbering just 1 less than the length of 'text'
    # in 'midLett'(to perfectly fit as the filling alphabets)
    # then the program extracts the letters of 'text' one by one,
    # adds to their ordinal value the value of 'key'
    # then converts that new value to char(in unicode)
    # then it adds that new character to the temp variable.
    # The letters in midLett act as as a
    # filling between the letters of 'temp'.
    from getTime import preciseTimestamp
    from randWord import genrt
    key = genrtNum(3)
    midLett = []  # stores the list of random small characters

    # generate a random character and append it to the empty list 'midLett'
    for x in range(0, len(text)-1):
        midLett.append(genrt(1))

    temp = ""  # this will store the encrypted string temporarily

    for i in range(0, len(text)):
        # this adds to the ordinal value of text's character the value of 'key'
        val = ord(text[i]) + key
        if i == 0:  # if i is 0 only concatenate the empty 'temp' and the unique chracter
            temp = temp + chr(val)
        else:
            # characters of 'midLett' acting as filling
            temp = temp + midLett[i - 1] + chr(val)

    finalMidLett = ""

    for i in midLett:  # converts the list of random characters in midLett to a single string
        finalMidLett = finalMidLett+i

    encryptedText = temp
    # returns the key with val of 'key' and finalMidLett
    finalKey = str(key)+"~"+finalMidLett
    data = [encryptedText, finalKey]

    return data


for i in range(0, 6):
    x = genrt(6)
    print("Text: ", x, "  |  Encrypted: ", encrypt(x))
    print()
