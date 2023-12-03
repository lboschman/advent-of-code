import re


class Puzzle:
    max_red = 12
    max_green = 13
    max_blue = 14

    def __init__(self) -> None:
        self.id: int = 0
        self.val_dict = {
            "red": 0,
            "green": 0,
            "blue": 0,
        }

    def parse_line(self, line: str):
        self.set_id(line)
        games = line.split(":")[1].split(";")
        for game in games:
            self.parse_game(game)

    def set_id(self, line):
        id_parser = re.compile("(?<=Game )[0-9]+")
        self.id = int(id_parser.findall(line)[0])

    def parse_game(self, game):
        for color in self.val_dict.keys():
            match_pattern = f"([0-9]+)(?=\\s{color})"
            parser = re.compile(match_pattern)
            for i in parser.findall(game):
                self.val_dict.update({color: max(self.val_dict[color], int(i))})

    def is_possible(self):
        if ((self.val_dict["red"] <= self.max_red) 
        and (self.val_dict["green"] <= self.max_green) 
        and (self.val_dict["blue"] <= self.max_blue)):
            return self.id
        else:
            return 0

    def power(self):
        pwr = 1
        for value in self.val_dict.values():
            pwr *= value

        return pwr

with open("input.txt", "r") as file:
    lines = file.readlines()

value = 0
power = 0
for line in lines:
    game = Puzzle()
    game.parse_line(line)
    value += game.is_possible()
    power += game.power()

print(value)
print(power)
