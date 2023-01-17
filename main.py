import random
import time

MAX_HANDS = 3

MIN_BET = 1
MAX_BET = 100


def play_blackjack():  # main gameplay loop
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
    dealer_cards = [0, starting_cards[3]]
    hidden_card = starting_cards[2]
    hidden_card_up = False

    while True:
        soft17 = False
        player_total, soft17 = add_cards(player_cards)
        dealer_total, soft17 = add_cards(dealer_cards)
        print("Dealer's cards:", end=" ")
        if not hidden_card_up:
            print("?", end=" ")
        for card in dealer_cards:
            if card == 0:
                continue
            print(card, end=" ")
        print("")
        print("Your cards:", end=" ")
        for card in player_cards:
            print(card, end=" ")
        print("")
        if player_total == 21:
            if not hidden_card_up:
                print("You got 21!")
                hidden_card_up = True
                dealer_cards[0] = hidden_card
                continue
        elif player_total > 21:
            print("You busted!")
            dealer_cards[0] = hidden_card
            hidden_card_up = True
            return 1

        time.sleep(2)

        # dealer draws (must hit on soft 17 and lower)
        if hidden_card_up:
            if dealer_total < 17 or soft17:  # hit in case of soft 17 or less than 17
                dealer_cards.append(get_cards(deck, 1)[0])
                continue
            elif dealer_total > 21:
                print("Dealer bust!")
                return 0
            else:
                if player_total > dealer_total:
                    return 0
                elif player_total == dealer_total:
                    return 3
                else:
                    return 1

                    # player action
        decision = input("What would you like to do? (s/h/d): ")
        if decision == "s":  # stand
            dealer_cards[0] = hidden_card
            hidden_card_up = True
        elif decision == "h":  # hit
            player_cards.append(get_cards(deck, 1)[0])
        else:  # double
            player_cards.append(get_cards(deck, 1)[0])


def add_cards(cards):  # return total value of a hand of cards plus boolean for soft 17 total
    sum = 0
    soft17 = False
    ace_present = False
    for card in cards:
        card = str(card)
        if card.isdigit():
            sum += int(card)
        elif card == "A":
            sum += 1
            ace_present = True
        else:
            sum += 10

    if ace_present and sum + 10 <= 21:  # we only need to keep track of at least one ace present because others will count as 1 anyways
        if sum + 10 == 17:
            return 17, True
        else:
            return sum + 10, False

    return sum, False


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


def get_bet():  # how much does the user want to bet?
    while True:
        amount = input("How much would you like to bet? $")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f"Amount must be between ${MIN_BET} - ${MAX_BET}.")
        else:
            print("Please enter a number.")
    return amount


def main():  # allows player to start new games, make deposits, make bets
    balance = deposit()
    while True:
        bet = get_bet()

        if bet > balance:
            print(
                f"You do not have enough to bet that amount. Your current balance is: ${balance}.")
        else:
            break
    print(
        f"You are betting ${bet}. ")

    while True:
        result = play_blackjack()
        # RETURN TYPES
        # 0 = win, 1 = loss, 2 = double win, 3 = push
        if result == 0:
            print("WIN")
            print(f"You gained ${bet}!")
            balance += bet
        elif result == 1:
            print("LOSS")
            print(f"You lost ${bet}...")
            balance -= bet
        elif result == 3:
            print("PUSH")
            print("Bet returned.")

        print(f"Your total balance is ${balance}")

        if balance == 0:
            print(
                "Oh no! Game over.")

        while True:
            play_again = input("Play again (y/n): ")
            if play_again == "y" or play_again == "n":
                break
            else:
                print("Not a valid input.")
        if play_again == "n":
            break


main()
