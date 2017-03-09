import math
def encryptMessageWithTextKey(message,textKey):
    key = generateKey(textKey)
    return encrypt(message,key)

def encrypt(message, key):
    if 0 <= len(key) <= 1:
        return message

    columns = len(key)
    blocks = (columns + 1)/2 * columns
    rows = int(math.ceil(len(message)/blocks)*columns)
    matrix = initMatrix(rows,columns)

    row = 0
    index = 0
    while index < len(message):
        for valueKey in range(0,key[row % columns]+1):
            try:
                matrix[row][valueKey] = message[index]
                index = index + 1
            except IndexError:
                1
        row = row + 1
    encryptedMessage = ''
    for i in range(columns):
        for j in range(rows):
            # if not(matrix[j][key[i]] == '\0'):
                encryptedMessage = encryptedMessage + matrix[j][key[i]]
    return encryptedMessage

def initMatrix(numberRows,numberColumns):
    matrix = []
    for row in range(numberRows):
        matrix.append([])
        for column in range(numberColumns):
            matrix[row].append('')
    return matrix

def decryptMessageWithTextKey(message,textKey):
    key = generateKey(textKey)
    return decrypt(message,key)

def generateKey(textKey):
    textKey = textKey.upper()
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    key = []
    #todo CONVENIENCE -> [0 9 6 10 2 7 5 3 8 1 4] ~ []
    for letter in alphabet:
        for indexKey in range(len(textKey)):
            if letter == textKey[indexKey]:
                key.append(indexKey)
    return key

def decrypt(message, key):
    columns = len(key)
    blocks = (columns + 1) / 2 * columns
    rows = int(math.ceil(len(message) / blocks) * columns)
    matrix = initMatrix(rows, columns)
    size = 0
    for r in range(rows):
        for c in range(key[r%columns]+1):
            if size < len(message):
                size = size + 1
                matrix[r][c] = 'X'
    k = 0
    for c in range(columns):
        for r in range(rows):
            if(matrix[r][key[c%columns]]=='X'):
                matrix[r][key[c%columns]] = message[k]
                k = k + 1

    decryptMessage = ''
    for r in range(rows):
        for c in range(columns):
            decryptMessage = decryptMessage + matrix[r][c]
    return decryptMessage

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
print(cryptedMessage)
print(decryptMessageWithTextKey(cryptedMessage,key))