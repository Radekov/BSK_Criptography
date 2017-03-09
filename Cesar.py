def encryptCesarA(message, k):
    if not isPrimeNumber(k):
        return message
    cryptedMessage = ""
    firstAlphabetLetter = ord('A')
    lenghtAlphabet = 26
    message = message.upper()

    for letter in message:
        if not ('A' <= letter <= 'Z'):
            cryptedMessage += letter
            continue
        cryptedMessage += chr((ord(letter) + k - firstAlphabetLetter) % lenghtAlphabet + firstAlphabetLetter)

    return cryptedMessage

def encryptCesarB(message, k1, k0):
    if not (isPrimeNumber(k0) and isPrimeNumber(k1)):
        return message
    cryptedMessage = ""
    firstAlphabetLetter = ord('A')
    lenghtAlphabet = 26
    message = message.upper()

    for letter in message:
        if not ('A' <= letter <= 'Z'):
            cryptedMessage += letter
            continue
        cryptedMessage += chr((ord(letter) *k1 + k0 - firstAlphabetLetter) % lenghtAlphabet + firstAlphabetLetter)

    return cryptedMessage


def isPrimeNumber(number):
    # number = int(input("Enter a number: "))
    if number > 1:
        for i in range(2, number):
            if (number % i) == 0:
                print(number, "nie jest liczba pierwsza")
                return False
        else:
            return True
    else:
        return False

def decryptCesarB(crypted, k1, k0):
    if not (isPrimeNumber(k0) and isPrimeNumber(k1)):
        return crypted
    crypted = crypted.upper()
    encryptedMessage = ''
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    power = pow(k1,11)

    for letter in crypted:
        if not ('A' <= letter <= 'Z'):
            encryptedMessage += letter
            continue
        index = (valueLetter(letter) + len(alphabet) - k0)*power % len(alphabet)
        encryptedMessage += alphabet[index]

    return encryptedMessage

def valueLetter(letter):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for l in range(0,len(alphabet)):
        if alphabet[l] == letter:
            return l

print("Podaj wiadomość do zaszyfrowania")
message = input()
print("Podaj liczbe pierwsza k1")
k1 = input()
k1 = int(k1)
print("Podaj liczbe pierwsza k0")
k0 = input()
k0 = int(k0)
cryptedMessage = encryptCesarB(message,k1,k0)
print("Zaszyfrowana:",cryptedMessage)

print("Rozszyfrowana:",decryptCesarB(cryptedMessage,k1,k0))