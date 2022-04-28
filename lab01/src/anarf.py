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


# todo find a^ and finish code below


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

    for character in cryptogram:
        a = ord(character)
        if a in range(65, 91):
            a = a + key[0]
            while a > 90:
                a = a - 26
        if a in range(97, 123):
            a -= key
            if a < 97:
                a = a + 26
        message += chr(a)

    with open("data/decrypt.txt", "w") as f:
        f.write(message)

    return message


def find_key():
    with open("data/crypto.txt", "r") as f:
        cryptogram = f.read()
        cryptogram = cryptogram.replace('\n', ' ')

    with open("data/extra.txt", "r") as f:
        extra = f.read()
        extra = extra.replace('\n', ' ')
        extra = extra.split(" ")

    for index_word, word in enumerate(cryptogram):
        for index_character, character in enumerate(word):
            if ord(character) in range(65, 91) or ord(character) in range(97, 123):
                key = (ord(character) - ord(extra[index_word][index_character])) % 26
                with open("data/key-found.txt", "w") as f:
                    f.write(str(key))
                return key

    key = "Can't find a key :-("

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
