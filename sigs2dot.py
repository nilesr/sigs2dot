#!/usr/bin/env python3
import string, sys
def sanitize(s):
    final = ''
    for char in s:
        if char in string.ascii_letters:
            final += char
    return final
def sanitize2(s):
    for char in ["\""]:
        s = s.replace(char,"")
    return s
def get(label, second = False, rev = False):
    s = "\"" + sanitize2(label) + "\""
    if rev:
        s += '[color="red",label="revocation"]'
    return s
f = open(sys.argv[1], "r").read().split('\n')
inuid = False
print("digraph test {")
# print("\tsize=\"24,24\";")
# print("\tratio=1;")
print("\tgraph [overlap = false];")
for line in f:
    if "User ID not found" in line:
        continue
    if line[:3] == 'uid':
        inuid = True
        # current_id = " ".join(line.split()[1:])
        current_id = line[25:]
        continue
    elif line[:3] == 'sub':
        inuid = False
        continue
    if inuid:
        if line[:3] in ["sig", "rev"]:
            currentsig = line[42:]
            if currentsig in current_id:
                # Its a selfsig
                continue
            if "PGP Global Directory Verification Key" in currentsig:
                continue
            rev = line[:3] == "rev"
        else:
            continue
        print("\t" + get(currentsig) + " -> " + get(current_id, True, rev) + ";")
print("}")
