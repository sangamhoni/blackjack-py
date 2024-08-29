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
        card_names.append(str(card))
        card_values.append(card)

# custom function to print hands in proper format
def print_hands(card_names, card_values, player):
    hand_parts=[]
    
    for i in range(len(card_names)):
        card=card_names[i]
        value=card_values[i]
        hand_parts.append(f"{card} ({value})")
        # here, hand_parts is the list with the values stored as: ["Ace (11)", "Queen (10)", "7 (7)"]
    
    hand_str="    "+player+" hands: " + " + ".join(hand_parts)
    # here, .join() functions joins all the elements in the lsit hand_parts putting in " + " in between them
    # ie. hand_str = "Ace (11) + Queen (10) + 7 (7)"
    print(hand_str)

# custom func to adjust Aces to 1 if it's a 'Bust'
def adjust_ace(card_values):
    while (sum(card_values)>21 and 11 in card_values):     # Check if total is over 21 and if there's an Ace valued at 11
        card_values[card_values.index(11)]=1     # Change the Ace's value from 11 to 1

def win_check(card_values):
    card_sum=sum(card_values)
    
    if (card_sum==21):
        print("Congratulations! It's a BLACKJACK.")
        print("You win!")
        exit()
    elif (card_sum>21):
        print("\nIt's a BUST :(")
        print("Better luck next time!")
        exit()

# Taking User's name
user_name=input("What's your name? ").capitalize()

# Initial two hands
for i in range(0, 2):
    hit_card(user_cards, user_values)
    hit_card(dealer_cards, dealer_values)

# Print user's initial two hands
print_hands(user_cards, user_values, user_name)

# game_over=False

while (True):
    win_check(user_values)

    right_input = False

    while (not right_input):
        draw_card = input("\nDraw another card? (Y/N) ")
        # check if user gives the right input
        if (draw_card.lower() == "y" or draw_card.lower() == "n"):
            right_input = True
        
    if draw_card.lower() == "y":
        hit_card(user_cards, user_values)
        adjust_ace(user_values) # to fix if any aces are there and the sum exceeds 21
        print_hands(user_cards, user_values, user_name)
        win_check(user_values)
    else:
        user_card_sum=sum(user_values)
        print(f"\nFinal hand: ")
        print_hands(user_cards, user_values, user_name)
        break




    
    
    
    
    

# print_hands()


# if (my_card<0 or my_card>13):
#     print("BAD CARD")
# else:
#     print(f"Your hand value is {my_card}")


# Write code here to identify the value of each card.
# my_card=int(input(""))
# if (my_card<0 or my_card>13):
#     print("BAD CARD")
# elif (my_card==1):
#     print("Your hand value is 11.")
# elif (my_card>=10 and my_card<=13):
#     print("Your hand value is 10.")
# else:
#     print(f"Your hand value is {my_card}.")


# Write code here to print out the game outcome given a hand value.
# hand_value=int(input())
# if (hand_value==21):
#     print("BLACKJACK!")
# elif (hand_value<4 or hand_value>31):
#     print("BAD HAND VALUE!")
# elif (hand_value>21):
#     print("BUST.")
