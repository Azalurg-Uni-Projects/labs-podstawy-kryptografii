# Copyrights
# Patryk Wawrzyniak
import random
import sys

line_len = 64


def BinaryToDecimal(binary):
    binary1 = binary
    decimal, i, n = 0, 0, 0
    while binary != 0:
        dec = binary % 10
        decimal = decimal + dec * pow(2, i)
        binary = binary // 10
        i += 1
    return decimal


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
                line += "Z"
        line += "\n"
        f.write(line)
    return True


def generate_key():
    # alphabet = "QAZWSXEDCRFVTGBYHNUJMIKOLPqazwsxedcrfvtgbyhnujmikolp1234567890"
    alphabet = "QAZWSXEDCRFVTGBYHNUJMIKOLPqazwsxedcrfvtgbyhnujmikolp"
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

    with open("data/crypto.txt", "w") as f:
        pass

    for l in range(len(plain)):
        new_line = ""
        coded_line = ""
        line = ' '.join(format(ord(i), 'b') for i in plain[l])
        line = line.split(" ")
        for i in range(len(line)):
            while len(line[i]) != 8:
                line[i] = "0" + line[i]
        line = ''.join(format(x) for x in line)
        if line != "00000000":
            for i in range(len(line)):
                result = int(line[i]) ^ int(key[i])

                if result:
                    coded_line += "1"
                else:
                    coded_line += "0"
                new_line = new_line + str(result)
            with open("data/crypto.txt", "a") as f:
                f.write(new_line + '\n')
    return True


def krypto_analysis():
    with open("data/crypto.txt", "r") as f:
        text = f.read()
        text = text.replace("\n", "*")
        text = text.split("*")
        text.pop(len(text)-1)

    for index, line in enumerate(text):
        output = [line[i:i+8] for i in range(0, len(line), 8)]
        text[index] = output

    for row_index, row in enumerate(text):
        for column_index, column in enumerate(row):
            reset_char = False
            if len(column) > 1:
                if column[1] == "1":
                    reset_char = column
                if reset_char:
                    for i in range(len(text)):
                        coded_char = text[i][column_index]
                        coded_line = ""
                        for j in range(8):
                            result = int(coded_char[j]) ^ int(reset_char[j])
                            if result:
                                coded_line += "1"
                            else:
                                coded_line += "0"
                        if coded_line == "00000000":
                            text[i][column_index] = " "
                        else:
                            text[i][column_index] = chr(int(coded_line, 2))

    with open("data/decrypt.txt", "w") as f:
        for row in text:
            for column in row:
                f.write(column)
            f.write("\n")
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
    todo = krypto_analysis
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
