# create a list of all cards in a 52 card deck

# suit options
suit = ["hearts", "diamonds", "spades", "clubs"]

# royal cards
royal = ["king", "queen", "jack", "ace"]

# number values of the deck
numbers = []
for i in range(2, 11):
    numbers.append(i)  # loop through from 2 to before 11 i.e. 2 to 10

deck = []

# number/suit combinations e.g. 2 of spades
for n in numbers:
    for (
        s
    ) in (
        suit
    ):  # each number will loop through every suit before moving on to the next number
        deck.append(str(n) + " of " + s)  # str() so the numbers can be part of a string

# royal/suit combinations e.g. king of hearts
for r in royal:
    for s in suit:
        deck.append(str(r) + " of " + s)

print(len(deck))  # confirm 52 items (cards) in the list
print(deck)  # confirm the 52 cards

