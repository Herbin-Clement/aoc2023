filename = "data.dat"

s = 0
with open(filename, "r") as f:
    lines = f.readlines()
    for line in lines:
        n = ""
        for c in line:
            if ord(c) >= ord("0") and ord(c) <= ord("9"):
                n += c
        
        s += int(n[0] + n[len(n) - 1])

print(s)