filename = "data.dat"

symbol = "0123456789."

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

def have_adj_symbol(grid, x, y, number, length, w, h):
    # print(number, x, y, length, w, h)
    for i in range(x-1, x+length+1):
        for j in range(y-1, y+2):
            if check(grid, i, j, w, h):
                return True


def check(grid, x, y, w, h):
    if x >= 0 and x < w and y >= 0 and y < h:
        # print(f"({y}, {x}) = {grid[y][x]}")
        return grid[y][x] not in symbol
    return False

s = 0
with open(filename, "r") as f:
    lines = f.readlines()
    h = len(lines)
    w = len(lines[0]) - 1
    numbers = []
    for i, line in enumerate(lines):
        numbers += find_number(line, i)
    for number in numbers:
        if have_adj_symbol(lines, number[0], number[3], number[1], number[2], w, h):
            print(number[1], number[3], number[0])
            s += number[1]

print(s)