import random
import time

# store hands with their names; data type=string
user_cards=[]
dealer_cards=[]
# store each card's values as it is wrt its original index; data type=integer
user_values=[]
dealer_values=[]

print("hi")

# custom function to get a new card
def hit_card(card_names, card_values):
    card=random.randint(1, 13)
    
    if (card==1):
        card_names.append("Ace")
        card_values.append(11)
    elif (card==11):
        card_names.append("Jack")
        card_values.append(10)
    elif (card==12):
        card_names.append("Queen")
        card_values.append(10)
    elif (card==13):
        card_names.append("King")
        card_values.append(10)
    else:
        card_names.append(card)
        card_values.append(card)

# custom function to print hands in proper format
def print_hands(card_names, card_values, player):
    hand_parts=[]
    
    for i in range(len(card_names)):
        card=card_names[i]
        value=card_values[i]
        
        if (type(card)==str):
            hand_parts.append(f"{card} ({value})")
        elif (type(card)==int):
            hand_parts.append(f"{card}")
        # here, hand_parts is the list with the values stored as: ["Ace (11)", "Queen (10)", "7 (7)"]
    
    hand_str="    "+player+" hand: " + " + ".join(hand_parts)
    # here, .join() functions joins all the elements in the lsit hand_parts putting in " + " in between them
    # ie. hand_str = "Ace (11) + Queen (10) + 7 (7)"
    print(hand_str)

# custom func to adjust Aces to 1 if it's a 'Bust'
def adjust_ace(card_values):
    while (sum(card_values)>21 and 11 in card_values):     # Check if total is over 21 and if there's an Ace valued at 11
        card_values[card_values.index(11)]=1     # Change the Ace's value from 11 to 1

def win_check(card_values, player):
    card_sum=sum(card_values)
    
    if (card_sum==21):
        time.sleep(1)
        print("\n--------------------------------------------------")
        print("\nIT IS A BLACKJACK!")
        if (player!="Dealer"):
            print("Congratulations! You win!\n")
        else:
            print(f"{player} wins the game.\n")
        exit()
    elif (card_sum>21):
        time.sleep(1)
        print("\n--------------------------------------------------")
        print("\nIT IS A BUST :(")
        if (player!="Dealer"):
            print("Better luck next time!\n")
        else:
            
            print("You win the game!\n")
        exit()

# Taking User's name & Setting's Dealer's name
user_name=input("What's your name? ").capitalize()
dealer_name="Dealer"

# Initial two hands
for i in range(0, 2):
    hit_card(user_cards, user_values)
    hit_card(dealer_cards, dealer_values)

# Print user's initial two hands
print("\n--------------------------------------------------")
print(f"INITIAL HAND: ")
print_hands(user_cards, user_values, user_name)

# game_over=False

while (True):
    # checking for blackjack or bust
    win_check(user_values, user_name)
    right_input = False

    while (not right_input):
        draw_card = input("\nHit another card? (Y/N) ")
        # check if user gives the right input
        if (draw_card.lower() == "y" or draw_card.lower() == "n"):
            right_input = True
        
    if draw_card.lower() == "y":
        hit_card(user_cards, user_values)
        adjust_ace(user_values) # to fix if any aces are there and the sum exceeds 21
        print_hands(user_cards, user_values, user_name)
        win_check(user_values, user_name)
    else:
        print(f"\n{user_name} stands!")
        time.sleep(1)
        user_card_sum=sum(user_values)
        print(f"\nFINAL HAND: ")
        print_hands(user_cards, user_values, user_name)
        break

# Dealer Side Hand                                      
game_decision=True
time.sleep(1)
print("\n--------------------------------------------------")
print("--------------------------------------------------")
print(f"INITIAL HAND: ")
print_hands(dealer_cards, dealer_values, dealer_name)
win_check(dealer_values, dealer_name)

while (game_decision):
    dealer_card_sum=sum(dealer_values)
    
    print(f"\n{dealer_name} thinking...")
    time.sleep(3)
    if (dealer_card_sum<17):
        print(f"\n{dealer_name} hits!")
        time.sleep(1)
        hit_card(dealer_cards, dealer_values)
        adjust_ace(dealer_values)
        print_hands(dealer_cards, dealer_values, dealer_name)  
        win_check(dealer_values, dealer_name)
        
    elif (dealer_card_sum>=17):
        print(f"\n{dealer_name} stands!")
        time.sleep(1)
        print("\n--------------------------------------------------")
        print("FINAL HAND:")
        print_hands(user_cards, user_values, user_name)
        print_hands(dealer_cards, dealer_values, dealer_name)  
        print("")
        if (dealer_card_sum==user_card_sum):
            print("It's a Push (Tie).\n")
        elif (dealer_card_sum>user_card_sum):
            print(f"{dealer_name} wins the game.\n")
        elif (dealer_card_sum<user_card_sum):
            print(f"{user_name} wins the game.\n")
        exit()
