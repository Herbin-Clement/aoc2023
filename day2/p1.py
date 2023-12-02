filename = "data.dat"

m = {
    "red": 12,
    "green": 13,
    "blue": 14
}

def check(line):
    for set in line.split(";"):
        for game in set.split(","):
            cube = game.split(" ")
            color = cube[2].replace("\n", "")
            v = int(cube[1])
            if v > m[color]:
                return False
    return True

s = 0
with open(filename, "r") as f:
    lines = f.readlines()
    n = len(lines)
    s = n * (n + 1) // 2
    for i, line in enumerate(lines):
        line = line.split(":")[1]
        if not check(line):
            s -= i + 1

print(s)