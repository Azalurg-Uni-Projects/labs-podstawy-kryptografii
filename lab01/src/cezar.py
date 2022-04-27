def szyfrowanie():
    with open("data/plain.txt", "r") as f:
        text = f.read()
        text = text.replace('\n', ' ')

    with open("data/key.txt", 'r') as f:
        K = int(f.readline().split(" ")[0])
        K = K % 26

    text = text.lower()  # zmiana wilkości liter na małe
    S = ""

    for znak in text:
        if znak != " ":
            a = ord(znak) + K  # przekonwertowanie 1 zaku widomości na liczbę dziesiętną i dodani klucza
            if a > 122:
                a = a - 26
        else:
            a = 32
        S += chr(a)

    with open("data/crypto.txt", "w") as f:
        f.write(S)

    return S

def odszyfrowanie():
    with open("data/crypto.txt", "r") as f:
        text = f.read()
        text = text.replace('\n', ' ')

    with open("data/key.txt", 'r') as f:
        K = int(f.readline().split(" ")[0])
        K = K % 26

    text = text.lower()  # zmiana wilkości liter na małe
    S = ""

    for znak in text:
        if znak != " ":
            a = ord(znak) - K  # przekonwertowanie 1 zaku widomości na liczbę dziesiętną i dodani klucza
            if a < 97:
                a = a + 26
        else:
            a = 32
        S += chr(a)

    with open("data/decrypt.txt", "w") as f:
        f.write(S)

    return S
