filename = "data.dat"

def find_number(line, index):
    i = 0
    res = []
    curr_number = []
    start_index = -1
    while i < len(line):
        c = line[i]
        if c.isdigit():
            start_index = i
            curr_number.append(c)
            i += 1
            c = line[i]
            while c.isdigit():
                curr_number.append(c)
                i += 1
                c = line[i]
            res.append((start_index, int("".join(curr_number)), len(curr_number), index))
            curr_number = []
        i += 1
    return res

def find_adj_symbol(grid, x, y, number, length, w, h, d):
    for i in range(x-1, x+length+1):
        for j in range(y-1, y+2):
            if check_star(grid, i, j, w, h):
                key = f"{i}.{j}"
                if d.get(key, None):
                    d[key].append(number)
                else:
                    d[key] = [number]



def check_star(grid, x, y, w, h):
    if x >= 0 and x < w and y >= 0 and y < h:
        return grid[y][x] == "*"
    return False

s = 0
with open(filename, "r") as f:
    lines = f.readlines()
    h = len(lines)
    w = len(lines[0]) - 1
    numbers = []
    d = dict()
    for i, line in enumerate(lines):
        numbers += find_number(line, i)
    for number in numbers:
        find_adj_symbol(lines, number[0], number[3], number[1], number[2], w, h, d)
    for t in d.values():
        if len(t) == 2:
            s += t[0] * t[1]

print(s)