# Blackjack!
Blackjack is a popular gambling card game in which players attempt to make a hand as close as possible to a sum of 21 without going over.  

Each player is dealt an initial hand of 2 cards. The first player may then choose to "hit" (draw another card into their hand) or "stand" (keep their current hand), and play passes to the next player. A player may hit as many times as they want, but if they go over 21, they "bust" - or automatically lose.  

&nbsp;  

## Scoring
In determining hand totals, cards get the following values:  
1. All face cards (Jacks, Queens, and Kings) are worth 10.  
2. Aces can count as either 1 or 11, whatever is the best case for user to not get BUSTed.  
3. All other cards have the value shown on the card (ie 2 will be worth 2, 3 will be worth 3, and so on).  

&nbsp;  

## Outcomes  
Each player (excluding the dealer) has one of the three possible outcomes:  
- **Lose**: any player who busts or has a hand value less than the dealer, loses.  
- **Win**: any player who does not bust and has a hand value greater than the dealer, wins.  
- **Push**: any player who does not bust and has a hand value matching the dealer, pushes (ties).  

If you'd prefer a video explanation of the game, check one out [here](https://www.youtube.com/watch?v=qd5oc9hLrXg).  

&nbsp;  

## How to play
1. **Enter your name** to start the game.  
2. **Get your cards**: You and the dealer each get two cards.  
3. **Decide**:  
    - *Hit* to draw another card (*type "Y"*).  
    - *Hold* to keep your current hand (*type "N"*).  
4. **Check for a win**: The game checks for a Blackjack (21) or a Bust (over 21).
5. **Dealer's turn**: The dealer plays until their hand is 17 or higher.
6. **Final Result**: The closest hand to 21 wins. If it's a tie, it's a Push.
Good luck!



&nbsp;  

## Considerations and Features  
#### Error Handling:
- Manages invalid inputs and prompts for correct data if non-numeric or out-of-range values are entered.
- Alerts user if lowerbound is not less than upperbound.

#### User Experience:
- Provides feedback: "Try Again! You guessed too high" or "Try Again! You guessed too small."
- Congratulates on correct guesses; otherwise, gives "Better Luck Next Time!" if guesses exceed the limit.

#### Edge Cases:
- Handles scenarios with no valid numbers between bounds and ensures bounds are valid.

#### Input Validation:
- Ensures inputs are integers and within the valid range, guiding users to provide correct values.  

### Human Processing Time:  
- Breaks and Pauses are provided, letting users process the information first.  

&nbsp; 

## Implementation  
1. Lists are used to store your hands.  
2. two separate lists storing card names (Ace, Jack, King, etc), and another storing corresponding values (11 for Ace, 10 for Jack, King, and Queen, etc)
3. takes in consideration as Ace for both 11 and 1, Dynamic adjustment of ace's value
4. has user-defined function to minimize redundancy as much as possible
5. has a 'hand_parts' list which combines two lists 'user_cards' and 'card_values' into a sequence of paired tuples

&nbsp; 

## Future Improvement Checklists
1. Add Split function?  
2. Add Double Money function?
3. Make it multiplayer and online playable?  
4. Make some digital currency to bet money with?  
