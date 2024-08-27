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


