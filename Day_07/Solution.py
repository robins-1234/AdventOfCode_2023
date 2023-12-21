from enum import Enum


class Hand:
    class Hand_Type(Enum):
        FIVE_OF_A_KIND = 7
        FOUR_OF_A_KIND = 6
        FULL_HOUSE = 5
        THREE_OF_A_KIND = 4
        TWO_PAIR = 3
        ONE_PAIR = 2
        HIGH_CARD = 1

    def __str__(self) -> str:
        return str(self.name)

    def __init__(self, cards: str, bid: int):
        self.cards = cards
        self.bid = bid
        self.type = self.set_type(self.cards)
        self.value = self.type.value

    def set_type(self, cards) -> Hand_Type:
        if any(cards.count(card) == 5 for card in cards):
            return Hand.Hand_Type.FIVE_OF_A_KIND

        if any(cards.count(card) == 4 for card in cards):
            return Hand.Hand_Type.FOUR_OF_A_KIND

        if any(cards.count(card) == 3 for card in cards) & any(
            cards.count(card) == 2 for card in cards if cards.count(card) != 3
        ):
            return Hand.Hand_Type.FULL_HOUSE

        if any(cards.count(card) == 3 for card in cards):
            return Hand.Hand_Type.THREE_OF_A_KIND

        if sum(cards.count(card) // 2 for card in cards) > 2:
            return Hand.Hand_Type.TWO_PAIR

        if any(cards.count(card) == 2 for card in cards):
            return Hand.Hand_Type.ONE_PAIR

        return Hand.Hand_Type.HIGH_CARD

    def get_type(self) -> Hand_Type:
        return self.type

    def __repr__(self) -> str:
        return (
            "("
            + str(self.cards)
            + " "
            + str(self.type)
            + " "
            + str(self.value)
            + " "
            + str(self.bid)
            + ")"
        )

    def contains_multiple(cards: str, multiple: int) -> bool:
        return any(cards.count(card) == multiple for card in cards)


def sortKey(input: Hand, letters):
    key = (input.value,)
    for i in range(0, 5):
        key = key + (letters.index(input.cards[i]),)
    return key


def readInput():
    file = open("Day_07\input.txt", "r")
    result = file.readlines()
    file.close
    return result


def first(input: list):
    hands = []
    for line in input:
        cards = line.split(" ")[0]
        bid = line.split(" ")[1].split("\n")[0]
        hands.append(Hand(cards, bid))

    letters = ["A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2"]
    letters.reverse()

    hands = sorted(
        hands,
        key=lambda x: sortKey(x, letters),
    )

    result = 0
    for i in range(0, len(hands)):
        result = result + int(hands[i].bid) * (i + 1)

    return result


def second(input: list):
    print()


assert first(readInput()) == 249204891
second(readInput())
