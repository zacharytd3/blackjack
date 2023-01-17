import random

MAX_HANDS = 3

MIN_BET = 1
MAX_BET = 100


def play_blackjack():
    deck = {
        "2": 4,
        "3": 4,
        "4": 4,
        "5": 4,
        "6": 4,
        "7": 4,
        "8": 4,
        "9": 4,
        "10": 4,
        "J": 4,
        "Q": 4,
        "K": 4,
        "A": 4
    }
    starting_cards = get_cards(deck, 4)
    player_cards = [starting_cards[0], starting_cards[1]]
    dealer_cards = [starting_cards[2], starting_cards[3]]

    while True:
        print(f"Dealer's cards: ? {dealer_cards[1]}")
        print(f"Your cards:     {player_cards[0]} {player_cards[1]}")
        player_total = add_cards(player_cards)
        if player_total == 21:
            print("You got 21!")
            return 0
        elif player_total > 21:
            print("You busted!")
            return 1


def add_cards(cards):  # return total value of a hand of cards
    sum = 0
    for card in cards:
        if card.isdigit():
            sum += card
        elif card == "A":
            sum += 11  # CHANGE THIS IF IMPLEMENTING ACE
        else:
            sum += 10
    return sum


# returns a list of random cards from the deck, removes returned cards from deck
def get_cards(deck, num_cards):
    starting_cards = []
    for i in range(num_cards):
        new_card = random.choice(list(deck.keys()))
        if deck[new_card] > 0:
            deck[new_card] = deck[new_card] - 1
        else:
            del deck[new_card]  # not sure if del is the best function here
        starting_cards.append(new_card)
    return starting_cards


def deposit():  # deposit money before playing
    while True:
        amount = input("How much would you like to deposit? $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Amount must be greater than 0.")
        else:
            print("Please enter a number.")
    return amount


def get_number_of_hands():  # how many hands does the user want to play?
    while True:
        hands = input(
            "Enter the amount of hands to play (1-" + str(MAX_HANDS) + "): ")
        if hands.isdigit():
            hands = int(hands)
            if 1 <= hands <= MAX_HANDS:
                break
            else:
                print("Enter a valid number of hands.")
        else:
            print("Please enter a number.")
    return hands


def get_bet():  # how much does the user want to bet per hand?
    while True:
        amount = input("How much would you like to bet on each hand? $")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f"Amount must be between ${MIN_BET} - ${MAX_BET}.")
        else:
            print("Please enter a number.")
    return amount


def main():  # gameplay loop
    balance = deposit()
    hands = get_number_of_hands()
    while True:
        bet = get_bet()
        total_bet = bet*hands

        if total_bet > balance:
            print(
                f"You do not have enough to bet that amount. Your current balance is: ${balance}.")
        else:
            break
    total_bet = bet * hands
    print(
        f"You are betting ${bet} on {hands} hands. Total bet is equal to ${total_bet}. ")

    result = play_blackjack()


main()
