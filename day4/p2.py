filename = "data.dat"

s = 0
with open(filename, "r") as f:
    lines = f.readlines()
    copy = [1 for i in range(len(lines))]
    for i, line in enumerate(lines):
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
            for j in range(i + 1, i + counter +1):
                copy[j] += copy[i]
    s = sum(copy)
print(s)