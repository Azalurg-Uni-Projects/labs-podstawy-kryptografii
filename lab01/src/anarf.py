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
            a = a * key[1] + key[0]
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
            a = (a - key[0]) * key[1]
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
        cryptogram = cryptogram.replace(' ', '')

    with open("data/extra.txt", "r") as f:
        extra = f.read()
        extra = extra.replace('\n', ' ')
        extra = extra.replace(' ', '')
    # todo finish it

    key = "Can't find a key :-("
    for x in range(0, len(cryptogram) - 2):
        for y in range(0, len(extra) - 2):
            if ord(cryptogram[y]) > 91 or ord(cryptogram[x]) > 91:
                break
            a = (ord(cryptogram[y]) - ord(cryptogram[x]))*(ord(extra[y]) - ord(extra[x]))
            print(a)
            if a == 0:
                break
            #a = 1/a


            a = a % 26
            key = a
            with open("data/key-found.txt", "w") as f:
                f.write(str(key))
            return key
    return key


def break_code():
    message = ""
    with open("data/crypto.txt", "r") as f:
        cryptogram = f.read()
        cryptogram = cryptogram.replace('\n', ' ')
    with open("data/decrypt.txt", "w") as f:
        for key_b in range(1, 26):
            for key_a in [1, 3, 5, 7, 9, 11, 15, 17, 19, 21, 23, 25]:
                for character in cryptogram:
                    a = ord(character)
                    if a in range(65, 91):
                        a = (a - key_b) * key_a
                        while a > 90:
                            a = a - 26
                    if a in range(97, 123):
                        a = (a - key_b) * key_a
                        while a > 122:
                            a = a - 26
                    message += chr(a)
                message += "\n"
                f.write(message)
                message = ""

    return "Done"
