def code_message():
    cryptogram = ""

    with open("data/plain.txt", "r") as f:
        message = f.read()
        message = message.replace('\n', ' ')
        message = message.lower()

    with open("data/key.txt", 'r') as f:
        key = int(f.readline().split(" ")[0])
        key = key % 26

    for character in message:
        if character != " ":
            a = ord(character) + key
            if a > 122:
                a = a - 26
        else:
            a = 32
        cryptogram += chr(a)

    with open("data/crypto.txt", "w") as f:
        f.write(cryptogram)

    return cryptogram


def read_code():
    message = ""
    with open("data/crypto.txt", "r") as f:
        cryptogram = f.read()
        cryptogram = cryptogram.replace('\n', ' ')
        cryptogram = cryptogram.lower()

    with open("data/key.txt", 'r') as f:
        key = int(f.readline().split(" ")[0])
        key = key % 26

    for character in cryptogram:
        if character != " ":
            a = ord(character) - key
            if a < 97:
                a = a + 26
        else:
            a = 32
        message += chr(a)

    with open("data/decrypt.txt", "w") as f:
        f.write(message)

    return message
