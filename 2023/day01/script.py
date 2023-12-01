import re

with open("input.txt", "r") as file:
    lines = file.readlines()

total_part1 = 0

for line in lines:
    digits = [c for c in line if c.isdigit()]
    total_part1 += int(digits[0] + digits[-1])

print(f"The total of all coordinates is: {total_part1}")

numbers = {
    "zero": 0,
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}

pattern = re.compile("(?=(" + "|".join(numbers.keys()) + "|[0-9]))")


def to_number(value):
    try:
        return numbers[value]
    except KeyError:
        return int(value)


def get_number(line):
    values = pattern.findall(line)
    return 10 * to_number(values[0]) + to_number(values[-1])


total_part2 = 0
for line in lines:
    total_part2 += get_number(line)

print(f"The updated total of all coordinates is: {total_part2}")
