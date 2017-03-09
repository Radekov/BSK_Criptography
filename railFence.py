def encryptRailFence(message, numRails):
    if numRails == 1:
        return message
    rail = arrayStringsRows(message,numRails)
    # print(rail)
    cipher = ''
    for row in range(numRails):
        cipher=cipher+rail[row]
    return cipher

def decryptRailFence(cryptedMessage, numRails):
    if numRails <= 1 or len(cryptedMessage) < numRails:
        return cryptedMessage
    crail = arrayStringsRows(cryptedMessage,numRails)
    # print(crail)

    countRail = []
    for row in range(numRails):
        countRail.append(0)

    for row in range(numRails):
        countRail[row] = len(crail[row])

    rail = []
    for row in range(numRails):
        rail.append([])

    begin = 0
    for row in range(0,numRails):
        end = begin + countRail[row]
        rail[row] = list(cryptedMessage[begin:end])
        begin = end
    encryptedMessage = ''
    row = 0
    dir = 1
    # print(rail)
    for i in range(len(cryptedMessage)):
        encryptedMessage = encryptedMessage + rail[row].pop(0)
        row = row + dir
        if  row == numRails:
            dir=-1
            row=row-2
        if row==-1:
            dir=1
            row=row+2

    return encryptedMessage

def arrayStringsRows(message, numRails):
    rail = []
    for row in range(numRails):
        rail.append('')

    row = 0
    dir = 1
    for ch in message:
        rail[row] = rail[row] + ch
        row = row + dir
        if row == numRails:
            dir = -1
            row = row - 2
        if row == -1:
            dir = 1
            row = row + 2
    return rail

print("Podaj wiadomość do zaszyfrowania")
message = input()
print("Podaj liczbe plotkow")
numRails = input()
numRails = int(numRails)

cryptedMessage = encryptRailFence(message, numRails)
print("Zaszyfrowana:",cryptedMessage)

print("Rozszyfrowana:",decryptRailFence(cryptedMessage,numRails))