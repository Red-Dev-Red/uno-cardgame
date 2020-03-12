from random import randint



NAMES = ["Anna", "BertDeVaan", "Cameron", "DickDickson"]

class StandardCard:
    def __init__(self, c, n):
        self.color = c
        self.number = n

    def __str__(self):
        return self.color + " " + str(self.number)
    __repr__ = __str__


class WildPickColor:
    def __init__(self):
        pass

    def __str__(self):
        return "Wild Pick Color"
    __repr__ = __str__

class WildDrawFour:
    def __init__(self):
        pass

    def __str__(self):
        return "Wild Draw 4"
    __repr__ = __str__


class ReversCard:
    def __init__(self, c):
        self.color = c

    def __str__(self):
        return self.color + "Reverse"
    __repr__ = __str__


class SkipCard:
    def __init__(self, c):
        self.color = c

    def __str__(self):
        return self.color + "Skip"
    __repr__ = __str__


class DrawCard:
    def __init__(self, c):
        self.color = c

    def __str__(self):
        return self.color + "Draw 2"
    __repr__ = __str__


class Player:
    def __init__(self, name, pid):
        self.name = name
        self.pid = pid
        self.hand = []

class Deck:
    def __init__(self):
        self.deck = self.create_deck()

    def create_deck(self):
        deck = []
        for color in ['Blue', 'Green', 'Red', 'Yellow']:
            for num in range(1, 10):
                for _ in range(2):
                    card = StandardCard(color, num)
                    deck.append(card)
            card = StandardCard(color, 0)
            deck.append(card)

        for card in [WildDrawFour, WildPickColor]:
            for _ in range(4):
                deck.append(card())
        return deck
    
    def deal(self, player, amount):
        for i in range(amount):
            if len(self.deck) == 0:
                return
            i = randint(0, len(self.deck)-1)
            player.hand.append(self.deck[i])
            self.deck.remove(self.deck[i])


if __name__ == '__main__':
    deck = Deck()
    players = []

    for i, player in enumerate(NAMES):
        players.append(Player(player, i))
    
    for player in players:
        deck.deal(player, 7)
    
    for player in players:
        print(f"{player.name}: {player.hand}")
    # discard_pile = create_discard_pile(deck)
    # print(discard_pile[-1])
    print(deck.deck)

