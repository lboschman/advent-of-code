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
            return 2 ** (count_winners - 1)
        else:
            return 0

    def winner_count(self):
        return len([num for num in self.numbers if num in self.winners])


with open("input.txt", "r") as file:
    lines = file.readlines()

lines = [line[:-1] for line in lines]

cards = [ScratchCard(line) for line in lines]

scores = [card.get_score() for card in cards]

print(sum(scores))

cd = {card.id: [card, 1] for card in cards}


def process_card(i, card_dict):
    card, number = card_dict[i]
    winning_numbers = card.winner_count()
    for _ in range(number):
        for j in range(1, winning_numbers + 1):
            card_dict[i + j][1] += 1
    return card_dict


for i in list(cd.keys()):
    cd = process_card(i, cd)

print(sum([item[1] for item in cd.values()]))
