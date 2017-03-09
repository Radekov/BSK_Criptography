import math
def encrypt(message, key):
    if 0 <= len(key) <= 1:
        return message

    rows = initRows( math.ceil(len(message) / len(key)))
    rows = fillRows(rows,message,len(key))

    encryptedMessage = ''
    invKey = invPerm(key)
    for row in rows:
        for kIndex in range(len(invKey)):
            if len(row) > invKey[kIndex]:
                encryptedMessage = encryptedMessage + row[invKey[kIndex]]

    return encryptedMessage

def decrypt(message, key):
    numberRows = math.ceil(len(message) / len(key))
    rows = initRows(numberRows)
    rows = fillRows(rows,message,len(key))

    decryptedMessage = ''
    delRow = 0
    if len(message) % len(key) != 0:
        delRow = 1
    for row in range(len(rows) - delRow):
        for valueKey in key:
            decryptedMessage = decryptedMessage + rows[row][valueKey]


    lastRow = message[(numberRows-1)*len(key):]
    lastRow = fixLastRow(lastRow,key)
    decryptedMessage = decryptedMessage + lastRow
    return decryptedMessage

def initRows(numberRows):
    rows = []
    for row in range(numberRows):
        rows.append('')
    return rows
def fillRows(rows,message,lengthKey):
    numberRows = len(rows)
    for row in range(numberRows):
        rows[row] = message[row*len(key):(row+1)*len(key)]
    return rows
def invPerm(perm):
    inverse = [0] * len(perm)
    for i, p in enumerate(perm):
        inverse[p] = i
    return inverse
def fixLastRow(lastRow,key):
    length = len(lastRow)
    if length == len(key):
        return ''
    result = ''
    if 1<= length <=2:
        result = result + lastRow[0]
        if length == 2:
            result = result + lastRow[1]
        return result
    if length == 3:
        result = result + lastRow[1]
        result = result + lastRow[2]
        result = result + lastRow[0]
        return result
    print(lastRow)
    if length == 4:
        result = result + lastRow[1]
        result = result + lastRow[2]
        result = result + lastRow[0]
        result = result + lastRow[3]
        return result

key = [2,3,0,4,1]
print("Podaj wiadomość do zaszyfrowania")
message = input()
cryptedMessage = encrypt(message,key)
print(cryptedMessage)
print(decrypt(cryptedMessage,key))