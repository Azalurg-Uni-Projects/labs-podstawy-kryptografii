import sys
from src import cezar, anarf
s1, s2 = sys.argv[1], sys.argv[2]

if s1 in ["-c", "c"]:
    code = cezar
elif s1 in ["-a", "a"]:
    code = anarf
else:
    print("Wrong parameter: {}".format(s1))
    exit()

if s2 in ["-e", "e"]:
    print(code.code_message())
elif s2 in ["-d", "d"]:
    print(code.read_code())
elif s2 in ["-j", "j"]:
    print(code.find_key())
elif s2 in ["-k", "k"]:
    print(code.break_code())
else:
    print("Wrong parameter: {}".format(s2))