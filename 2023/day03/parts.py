from typing import List
import re


class Point:
    def __init__(self, x, y, value) -> None:
        self.x = x
        self.y = y
        self.value = value

    def is_neighbour(self, other):
        if (abs(self.x - other.x) <= 1) and (abs(self.y - other.y) <= 1):
            return True
        else:
            return False


class PartNumber(Point):
    def __init__(self, x, y, x_max, value):
        super().__init__(x, y, value)
        self.x_max = x_max
        self.points: List[Point] = []
        for i in range(x, x_max + 1):
            self.points.append(Point(i, y, "n"))

    def is_neighbour(self, other: Point):
        for point in self.points:
            if point.is_neighbour(other):
                return True
        return False


number_regex = re.compile("[0-9]+")
symbol = re.compile(r"[^0-9.\n]")


def parse_numbers(line, numbers, y):
    result = number_regex.search(line)
    while result:
        new_number = PartNumber(
            x=result.start(), y=y, x_max=result.end() - 1, value=int(result.group())
        )
        numbers.append(new_number)
        result = number_regex.search(pos=result.end(), string=line)
    return numbers


def parse_symbols(line, points, y):
    result = symbol.search(line)
    while result:
        new_point = Point(x=result.start(), y=y, value=result.group())
        points.append(new_point)
        result = symbol.search(pos=result.end(), string=line)
    return points


def parse_line(line, numbers, points, line_number):
    numbers = parse_numbers(line, numbers, line_number)
    points = parse_symbols(line, points, line_number)
    return numbers, points


with open("input.txt", "r") as file:
    lines = file.readlines()


print(len(lines))
points = []
numbers = []

for i, line in enumerate(lines):
    numbers, points = parse_line(line, numbers, points, i)

value = 0

for number in numbers:
    for point in points:
        if number.is_neighbour(point):
            value += number.value
            break
print(value)
