with open("data/hash_coppy.txt", "r") as f:
    hashes = []
    for x in f:
        hashes.append(x.replace("\n", ""))

for x in range(0, len(hashes), 2):
    h1 = "{0:08b}".format(int(hashes[x], 16))
    h2 = "{0:08b}".format(int(hashes[x+1], 16))
    sum = 0
    dif = 0
    for x, y in zip(h1, h2):
        if (x != y):
            dif += 1
        sum += 1
    print(f"{str(dif)}/{str(sum)}", round(dif/sum, 2))
