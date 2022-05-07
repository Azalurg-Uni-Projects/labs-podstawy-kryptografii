import numpy as np

def find_prime(x):
    counter = 0
    while counter * x % 26 != 1:
        counter += 1
    return counter


def code_message():
    cryptogram = ""

    with open("data/plain.txt", "r") as f:
        message = f.read()
        message = message.replace('\n', ' ')

    with open("data/key.txt", 'r') as f:
        key = f.readline().split(" ")
        key[0], key[1] = int(key[0]), int(key[1])
        if key[0] < 0 or key[1] < 0:
            return "Wrong key: {}, {}".format(key[0], key[1])
        key[0] = key[0] % 26

    for character in message:
        a = ord(character)
        if a in range(65, 91):
            a = a*key[1] + key[0]
            while a > 90:
                a = a - 26
        if a in range(97, 123):
            a = a * key[1] + key[0]
            while a > 122:
                a = a - 26
        cryptogram += chr(a)

    with open("data/crypto.txt", "w") as f:
        f.write(cryptogram)

    return cryptogram


def read_code():
    message = ""
    with open("data/crypto.txt", "r") as f:
        cryptogram = f.read()
        cryptogram = cryptogram.replace('\n', ' ')

    with open("data/key.txt", 'r') as f:
        key = f.readline().split(" ")
        key[0], key[1] = int(key[0]), int(key[1])
        if key[0] < 0 or key[1] < 0:
            return "Wrong key: {}, {}".format(key[0], key[1])
        key[0] = key[0] % 26

    key[1] = find_prime(key[1])

    for character in cryptogram:
        a = ord(character)
        if a in range(65, 91):
            a = (a - key[0])*key[1]
            while a > 90:
                a = a - 26
        if a in range(97, 123):
            a = (a - key[0]) * key[1]
            while a > 122:
                a = a - 26
        message += chr(a)

    with open("data/decrypt.txt", "w") as f:
        f.write(message)

    return message


def find_key():
    with open("data/crypto.txt", "r") as f:
        cryptogram = f.read()
        cryptogram = cryptogram.replace('\n', ' ')
        cryptogram = cryptogram.split(" ")

    with open("data/extra.txt", "r") as f:
        extra = f.read()
        extra = extra.replace('\n', ' ')
        extra = extra.split(" ")
    # todo finish it

    for x in range(0, len(cryptogram)-2):
        for y in range(0, len(extra) - 2):
            a = (ord(cryptogram[x]) -ord( extra[y]))
          a = np.reciprocal()
    key = "Can't find a key :-("
    key = 3.0
    print(int(3.1) == 3.1)

    with open("data/key-found.txt", "w") as f:
        f.write(str(key))

    return key


def break_code():
    message = ""
    with open("data/crypto.txt", "r") as f:
        cryptogram = f.read()
        cryptogram = cryptogram.replace('\n', ' ')
    with open("data/decrypt.txt", "w") as f:
        for key in range(1, 26):
            for character in cryptogram:
                a = ord(character)
                if a in range(65, 91):
                    a -= key
                    if a < 65:
                        a = a + 26
                if a in range(97, 123):
                    a -= key
                    if a < 97:
                        a = a + 26
                message += chr(a)
            message += "\n"
            f.write(message)
            message = ""

    return "Done"
