# Copyrights
# Patryk Wawrzyniak

import random
import sys


def gcd(a, b):
    if a < b:
        return gcd(b, a)
    elif a % b == 0:
        return b
    else:
        return gcd(b, a % b)


def power_mod(a, b, c):
    x = 1
    y = a
    while b > 0:
        if b % 2 == 0:
            x = (x * y) % c
        y = (y * y) % c
        b = int(b / 2)
    return x % c


def power(a, b):
    x = 1
    y = a
    while b > 0:
        if b % 2 == 0:
            x = (x * y)
        y = (y * y)
        b = int(b // 2)
    return x


def key_gen():
    with open("data/elgamal.txt", "r") as f:
        p = int(f.readline().replace("\n", ''))
        g = int(f.readline().replace("\n", ''))
    private_key = random.randint(10 ** 20, p)
    while gcd(p, private_key) != 1:
        private_key = random.randint(10 ** 20, p)
    public_key = power_mod(g, private_key, p)

    with open("data/public.txt", "w") as f:
        f.write(str(p) + "\n" + str(g) + "\n" + str(public_key))

    with open("data/private.txt", "w") as f:
        f.write(str(p) + "\n" + str(g) + "\n" + str(private_key))

    print(f"Private-key: {private_key}\nPublic-key: {public_key}")
    return True


def encryption():
    with open("data/public.txt", 'r') as f:
        p = int(f.readline().replace("\n", ''))
        g = int(f.readline().replace("\n", ''))
        public_key = int(f.readline().replace("\n", ''))
    k = random.randint(10 ** 20, p)
    while gcd(p, k) != 1:
        k = random.randint(10 ** 20, p)

    with open("data/plain.txt", 'r') as f:
        msg = int(f.readline().replace("\n", " "))

    if not msg<p:
        return False

    with open("data/krypto.txt", "w") as f:
        f.write(str(power_mod(g, k, p)) + "\n" + str((power_mod(public_key, k, p) * msg)))

    return True


def decryption():
    with open("data/krypto.txt", "r") as f:
        gk = int(f.readline().replace("\n", ''))
        msg = int(f.readline().replace("\n", ''))

    with open("data/private.txt", "r") as f:
        p = int(f.readline().replace("\n", ''))
        g = int(f.readline().replace("\n", ''))
        b = int(f.readline().replace("\n", ''))

    key = power_mod(gk, b, p)
    with open("data/decrypt.txt", "w") as f:
        f.write(str(int(msg//key)))
    return True


def sign():
    with open("data/message.txt", "r") as f:
        msg = int(f.readline().replace("\n", ''))

    with open("data/private.txt", "r") as f:
        p = int(f.readline().replace("\n", ''))
        g = int(f.readline().replace("\n", ''))
        b = int(f.readline().replace("\n", ''))

    if not msg<p:
        return False

    k = random.randint(10 ** 20, p)
    while 1:
        k = random.randint(10 ** 20, p - 2)
        if gcd(k, p - 1) == 1:
            break

    r = power_mod(g, k, p)
    x = int(((msg - b*r)//k) % (p-1))
    with open("data/signature.txt", "w") as f:
        f.write(str(r) + "\n")
        f.write(str(x) + "\n")
        f.write(str(msg))
    return True


def verify():
    with open("data/public.txt", 'r') as f:
        p = int(f.readline().replace("\n", ''))
        g = int(f.readline().replace("\n", ''))
        public_key = int(f.readline().replace("\n", ''))

    with open("data/signature.txt", 'r') as f:
        r = int(f.readline().replace("\n", ''))
        x = int(f.readline().replace("\n", ''))
        msg = int(f.readline().replace("\n", ''))

    one = power_mod(g, msg, p)
    two = (power_mod(r, x, p)) * (power_mod(public_key, r, p))
    print(one == (two % p))
    with open("data/verify.txt", "w") as f:
        f.write(str(one == (two % p)))
    return True


s1 = sys.argv[1]

todo = False

if s1 in ["-k", "k"]:
    todo = key_gen
elif s1 in ["-e", "e"]:
    todo = encryption
elif s1 in ["-d", "d"]:
    todo = decryption
elif s1 in ["-s", "s"]:
    todo = sign
elif s1 in ["-v", "v"]:
    todo = verify
else:
    print("Wrong parameter: {}".format(s1))

if todo():
    print("Done")
else:
    print("ERROR !!!")

