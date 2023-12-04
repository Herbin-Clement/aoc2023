filename = "data.dat"

s = 0
with open(filename, "r") as f:
    lines = f.readlines()
    for line in lines:
        counter = 0
        numbers = dict()
        line = line.replace("\n", "")
        line = line.split(":")[1].split("|")
        wn = line[0].split(" ")
        mn = line[1].split(" ")
        for n in wn:
            if n != "":
                numbers[n] = True
        for n in mn:
            if n != "":
                if numbers.get(n, False):
                    counter += 1
        if counter > 0:
            s += 2 ** (counter - 1)
print(s)