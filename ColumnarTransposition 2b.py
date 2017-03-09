import math
def encryptMessageWithTextKey(message,textKey):
    key = generateKey(textKey)
    return encrypt(message,key)

def encrypt(message, key):
    if 0 <= len(key) <= 1:
        return message
    columns = initColumns(len(key))
    columns = fillColumns(columns, message, key)
    encryptedMessage = ''
    for k in key:
        encryptedMessage += columns[k]
    return encryptedMessage

def initColumns(numberColumns):
    columns = []
    for column in range(numberColumns):
        columns.append('')
    return columns

def fillColumns(columns, message, key):
    lengthKey = len(key)
    for indexMessage in range(len(message)):
        column = indexMessage%lengthKey
        columns[column] = columns[column] + message[indexMessage]
    return columns

def decryptMessageWithTextKey(message,textKey):
    key = generateKey(textKey)
    return decrypt(message,key)

def generateKey(textKey):
    textKey = textKey.upper()
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    key = []
    for k in range(len(textKey)):
        key.append(None)
    k = 0
    for letter in alphabet:
        for indexKey in range(0,len(textKey)):
            if letter == textKey[indexKey]:
                key[k] = indexKey
                k+=1
    return key

def decrypt(message, key):
    invert_key = invPerm(key)
    numberCol = len(key)
    columns = initColumns(numberCol)
    numberRows = math.ceil(len(message)/len(key))
    messLen = len(message)
    lettersInLastRow = messLen % numberCol
    sub = 0
    for k in range(numberCol):
        if key[k] < lettersInLastRow:
            columns[k] = message[sub:sub+numberRows]
            sub = sub + numberRows
        else:
            columns[k] = message[sub:sub+numberRows-1]
            sub = sub + numberRows - 1
    decryptedMessage = ''
    permutatedColumn = []
    for ik in invert_key:
        permutatedColumn.append(columns[ik])
    for index in range(numberRows):
        for col in range(numberCol):
            try:
                decryptedMessage = decryptedMessage + permutatedColumn[col][index]
            except IndexError:
                1
    return decryptedMessage

def invPerm(perm):
    inverse = [0] * len(perm)
    for i, p in enumerate(perm):
        inverse[p] = i
    return inverse


print("Podaj wiadomość do zaszyfrowania")
message = input()
print("Podaj klucz szyfrujący")
key = input()
cryptedMessage = encryptMessageWithTextKey(message,key)
print("Zaszyfrowana:",cryptedMessage)

print("Rozszyfrowana:",decryptMessageWithTextKey(cryptedMessage,key))