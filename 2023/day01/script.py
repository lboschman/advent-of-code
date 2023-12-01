import re

with open("input.txt", "r") as file:
    lines = file.readlines()

total_part1 = 0

for line in lines:
    digits = [c for c in line if c.isdigit()]
    total_part1 += int(digits[0] + digits[-1])

print(f"The total of all coordinates is: {total_part1}")
