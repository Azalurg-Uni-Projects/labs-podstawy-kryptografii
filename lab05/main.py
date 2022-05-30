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


def power(a, b, c):
    x = 1
    y = a
    while b > 0:
        if b % 2 == 0:
            x = (x * y) % c
        y = (y * y) % c
        b = int(b / 2)
    return x % c


def key_gen():
    with open("data/elgamal.txt", "r") as f:
        p = int(f.readline().replace("\n", ''))
        g = int(f.readline().replace("\n", ''))
    private_key = random.randint(10 ** 20, p)
    while gcd(p, private_key) != 1:
        private_key = random.randint(10 ** 20, p)
    public_key = power(g, private_key, p)

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

    with open("data/plain.txt", 'r') as f:
        msg = f.read()

    ct = []
    for i in range(0, len(msg)):
        ct.append(msg[i])

    for i in range(0, len(ct)):
        ct[i] = public_key * ord(ct[i])

    print(ord(msg)*public_key**17)
    return True

s1 = sys.argv[1]
todo = False

if s1 in ["-k", "k"]:
    todo = key_gen
elif s1 in ["-e", "e"]:
    todo = encryption
elif s1 in ["-d", "d"]:
    todo = False
elif s1 in ["-s", "s"]:
    todo = False
elif s1 in ["-v", "v"]:
    todo = False
else:
    print("Wrong parameter: {}".format(s1))

if todo():
    print("Done")
else:
    print("ERROR !!!")

# a = bool(1) # true 1
# b = bool(0)
# print(a^b)
#
# a = bool(1) # false 0
# b = bool(1)
# print(a^b)
