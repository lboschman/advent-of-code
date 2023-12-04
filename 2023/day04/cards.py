import re


class ScratchCard:
    def __init__(self, line: str):
        part1, part2 = line.split(":")
        part2, part3 = part2.split("|")
        self.id = self.get_id(part1)
        self.winners = self.read_numbers(part2)
        self.numbers = self.read_numbers(part3)

    def get_id(self, part1):
        try:
            return int(re.compile("[0-9]+").search(part1).group())
        except:
            return None

    def read_numbers(self, line):
        return [int(number) for number in line.split(" ") if number != ""]

    def get_score(self):
        count_winners = len([num for num in self.numbers if num in self.winners])
        if count_winners > 0:
            return 2**(count_winners-1)
        else:
            return 0


with open("input.txt", "r") as file:
    lines = file.readlines()

lines = [line[:-1] for line in lines]

cards = [ScratchCard(line) for line in lines]

scores = [card.get_score() for card in cards]

print(sum(scores))
