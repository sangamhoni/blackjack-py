import random

user_cards=[]
card_values=[]

# custom function to get a new card
def hit_card():
    card=random.randint(1, 13)
    
    if (card==1):
        user_cards.append("Ace")
        card_values.append(11)
    elif (card==11):
        user_cards.append("Jack")
        card_values.append(10)
    elif (card==12):
        user_cards.append("Queen")
        card_values.append(10)
    elif (card==13):
        user_cards.append("King")
        card_values.append(10)
    else:
        user_cards.append(card)
        card_values.append(card)


# custom function to print hands in proper format
def print_hands():
    hand_parts=[]
    
    for i in range(len(user_cards)):
        card=user_cards[i]
        value=card_values[i]
        hand_parts.append(f"{card} ({value})")
        # here, hand_parts is the list with the values stored as: ["Ace (11)", "Queen (10)", "7 (7)"]
    
    hand_str="Hand: " + " + ".join(hand_parts)
    # here, .join() functions joins all the elements in the lsit hand_parts putting in " + " in between them
    # ie. hand_str = "Ace (11) + Queen (10) + 7 (7)"
    print(hand_str)

# custom func to adjust Aces to 1 if it's a 'Bust'
def adjust_ace(card_values):
    while (sum(card_values)>21 and 11 in card_values):     # Check if total is over 21 and if there's an Ace valued at 11
        card_values.index(11)=1     # Change the Ace's value from 11 to 1



# Initial two hands
hit_card()
hit_card()

game_over=False

# while (not game_over):
    

print_hands()


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
