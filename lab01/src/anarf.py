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
    for x in range(0, len(extra) - 1):
        y1 = ord(cryptogram[x])
        y2 = ord(cryptogram[x+1])
        x1 = ord(extra[x])
        x2 = ord(extra[x+1])

        if x1 in range(65, 91) and x2 in range(97, 123) or x2 in range(65, 91) and x1 in range(97, 123):
            continue
        if x1 not in range(65, 91) and x1 not in range(97, 123):
            continue
        if x2 not in range(65, 91) and x2 not in range(97, 123):
            continue
        while x1 > 25:
            x1 -= 26
        while x2 > 25:
            x2 -= 26
        while y1 > 25:
            y1 -= 26
        while y2 > 25:
            y2 -= 26

        key_a = (y1 - y2)/(x1 - x2)


        if int(key_a) == key_a and int(key_a) > 0:
            print(x1, x2, y1, y2, key_a, end=" ")
            key_b = 0
            support = (x1*key_a+key_b) % 26
            while support != y1:
                support += 1
                key_b +=1
                if support > 25:
                    support -= 26
            print(key_b)
            with open("data/key-found.txt", "w") as f:
                f.write(f"{key_b} {int(key_a)}")
            return f"b: {key_b}, a: {int(key_a)}"
    return key


def break_code():
    message = ""
    with open("data/crypto.txt", "r") as f:
        cryptogram = f.read()
        cryptogram = cryptogram.replace('\n', ' ')
    with open("data/decrypt.txt", "w") as f:
        for key_b in range(1, 27):
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
