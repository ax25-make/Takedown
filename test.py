def read_data(filename):
    cards = {}
    with open(filename) as raw:
        for line in raw:
            line_cards = line.split()
            cards[line_cards[0]] = int(line_cards[1])
    return cards

cards = read_data("cards.txt")