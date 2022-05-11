# Copyrights
# Patryk Wawrzyniak
import random
import sys

line_len = 64


def prepare():
    with open("data/orig.txt", "r") as f:
        orig = f.read()
        orig = orig.upper()
        orig = orig.replace("\n", " ")
    line = ""
    with open("data/plain.txt", "w") as f:
        for index, ch in enumerate(orig):
            line += ch
            if (index + 1) % line_len == 0 and index != 0:
                line += "\n"
                f.write(line)
                line = ""

        if len(line) > 0:
            while len(line) != line_len:
                line += " "
        line += "\n"
        f.write(line)
    return True


def generate_key():
    # alphabet = "QAZWSXEDCRFVTGBYHNUJMIKOLPqazwsxedcrfvtgbyhnujmikolp1234567890"
    alphabet = "QAZWSXEDCRFVTGBYHNUJMIKOLP"
    with open("data/key.txt", "w") as f:
        for x in range(0, line_len):
            ch = random.randint(0, len(alphabet) - 1)
            f.write(alphabet[ch])
    return True


def code():
    with open("data/plain.txt", "r") as f:
        plain = f.read()
        plain = plain.replace("\n", "8")
        plain = plain.split("8")

    with open("data/key.txt", "r") as f:
        key = f.read()
        key = ' '.join(format(ord(i), 'b') for i in key)
        key = key.split(" ")
        for i in range(len(key)):
            while len(key[i]) != 8:
                key[i] = "0" + key[i]
        key = ''.join(format(x) for x in key)

    for l in range(len(plain)):
        new_line = ""
        bufor = ""
        line = ' '.join(format(ord(i), 'b') for i in plain[l])
        line = line.split(" ")
        for i in range(len(line)):
            while len(line[i]) != 8:
                line[i] = "0" + line[i]
        line = ''.join(format(x) for x in line)

        # todo https://www.geeksforgeeks.org/convert-binary-to-string-using-python/

        for i in range(len(line)):
            result = int(line[i]) ^ int(key[i])
            if result:
                bufor += "1"
            else:
                bufor += "0"
            if len(bufor) == 8:
                new_line += chr(int(bufor, 2))
                bufor = ""
        plain[l] = new_line
    print(plain)
    return True


s1 = sys.argv[1]
todo = False

if s1 in ["-p", "p"]:
    todo = prepare
elif s1 in ["-e", "e"]:
    todo = code
elif s1 in ["-g", "g"]:
    todo = generate_key
elif s1 in ["-k", "k"]:
    print("k")
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
