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





# Initial two hands
hit_card()
hit_card()

print_hands()