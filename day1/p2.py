filename = "data.dat"

s = 0
numbers = [
    ("one", "1"),
    ("two", "2"),
    ("three", "3"),
    ("four", "4"),
    ("five", "5"),
    ("six", "6"),
    ("seven", "7"),
    ("eight", "8"),
    ("nine", "9"),
]
with open(filename, "r") as f:
    lines = f.readlines()
    for line in lines:
        index_first = len(line)
        first = ""
        index_second = -1
        second = ""
        for number in numbers:
            index_f = line.find(number[0])
            if index_f != -1 and index_f < index_first:
                index_first = index_f
                first = number[1]
            index_l = line.rfind(number[0])
            if index_l != -1 and index_l > index_second:
                index_second = index_l
                second = number[1]
            index_f = line.find(number[1])
            if index_f != -1 and index_f < index_first:
                index_first = index_f
                first = number[1]
            index_l = line.rfind(number[1])
            if index_l != -1 and index_l > index_second:
                index_second = index_l
                second = number[1]
        s += int(f"{first}{second}")

print(s)