import sys
from src import cezar
s1, s2 = sys.argv[1], sys.argv[2]

if s1 in ["-c", "c"]:
    code = cezar
elif s1 in ["-a", "a"]:
    print("anarf")
else:
    print("error")

if s2 in ["-e", "e"]:
    print(code.szyfrowanie())
elif s2 in ["-d", "d"]:
    print(code.odszyfrowanie())
elif s2 in ["-j", "j"]:
    print("krypto z jawnym")
elif s2 in ["-k", "k"]:
    print("krypto bez jawnego")
else:
    print(error)