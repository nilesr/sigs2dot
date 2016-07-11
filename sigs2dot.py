import string, sys
def sanitize(s):
    final = ''
    for char in s:
        if char in string.ascii_letters:
            final += char
    return final
def get(label, second = False):
    # return sanitize(label) + " [label=\"" + label + "\"]"
    s = "\"" + label + "\""
    if not second: return s
    # return s +  " [minlen=2]"
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
        current_id = " ".join(line.split()[1:])
        continue
    elif line[:3] == 'sub':
        inuid = False
        continue
    if inuid:
        if line[:3] == "sig":
            currentsig = line[42:]
            if currentsig in current_id:
                # Its a selfsig
                continue
            if "PGP Global Directory Verification Key" in currentsig:
                continue
        else:
            continue
        print("\t" + get(currentsig) + " -> " + get(current_id, True) + ";")
print("}")
