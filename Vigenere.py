def encryptVinegere(message,key):
    message = message.upper()
    key = key.upper()
    if len(key) < len(message):
        key = extendKey(key,len(message))
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    cryptedMesssage = ''
    for letter in range(0,len(message)):
        if not ('A' <= message[letter] <= 'Z'):
            cryptedMesssage += message[letter]
            continue
        index = (valueLetter(message[letter]) + valueLetter(key[letter])) % len(alphabet)
        (alphabet.find(message[letter]) + alphabet.find(key[letter])) % len(alphabet)
        cryptedMesssage += alphabet[index]
    return cryptedMesssage

def extendKey(key, length):
    numbersOfLetter = len(key)
    index = 0
    while(len(key) < length):
        key += key[index]
        index = (index + 1) % numbersOfLetter
    return key

def valueLetter(letter):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for l in range(0,len(alphabet)):
        if alphabet[l] == letter:
            return l

def decryptVinegere(cryptedMessage, key):
    cryptedMessage = cryptedMessage.upper()
    key = key.upper()
    if len(key) < len(cryptedMessage):
        key = extendKey(key, len(cryptedMessage))
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    encryptedMessage = ''
    for letter in range(0,len(cryptedMessage)):
        if not ('A' <= cryptedMessage[letter] <= 'Z'):
            encryptedMessage += cryptedMessage[letter]
            continue
        index = (valueLetter(cryptedMessage[letter]) - valueLetter(key[letter])) % len(alphabet)
        (alphabet.find(cryptedMessage[letter]) - alphabet.find(key[letter])) % len(alphabet)
        encryptedMessage += alphabet[index]
    return encryptedMessage


print("Podaj wiadomość do zaszyfrowania")
message = input()
print("Podaj klucz szyfrujący")
key = input()
cryptedMessage = encryptVinegere(message,key)
print("Zaszyfrowana:",cryptedMessage)

print("Rozszyfrowana:",decryptVinegere(cryptedMessage,key))