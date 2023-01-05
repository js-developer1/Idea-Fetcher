from prettytable import PrettyTable

from fetch import cardData


def init():
    card = PrettyTable()
    card.field_names = [cardData['title']]
    card.add_row([cardData['desc']])
    print(card)

if __name__ == "__main__":
    init()