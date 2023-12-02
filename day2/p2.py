filename = "data.dat"

s = 0
with open(filename, "r") as f:
    lines = f.readlines()
    for i, line in enumerate(lines):
        r = 1
        d = {
            "red": 0,
            "green": 0,
            "blue": 0
        }
        line = line.split(":")[1]
        for set in line.split(";"):
            for game in set.split(","):
                cubes = game.split(" ")
                color = cubes[2].replace("\n", "")
                v = int(cubes[1])
                if d[color] < v:
                    d[color] = v
        print(d)
        for color in list(d.keys()):
            r *= d[color]
        s += r

print(s)