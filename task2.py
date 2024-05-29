import random

def display_choice(choice):
    choices = {
        'R': 'Rock',
        'P': 'Paper',
        'S': 'Scissors'
    }
    return choices.get(choice, 'Invalid choice')

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == 'R' and computer_choice == 'S') or \
         (user_choice == 'P' and computer_choice == 'R') or \
         (user_choice == 'S' and computer_choice == 'P'):
        return "You win!"
    else:
        return "Computer wins!"

def main():
    print("Welcome to Rock, Paper, Scissors Game!")
    choices = ['R', 'P', 'S']

    while True:
        print("\nEnter your choice:")
        print("R for Rock")
        print("P for Paper")
        print("S for Scissors")
        print("Q to Quit")

        user_choice = input("Your choice: ").upper()
        
        if user_choice == 'Q':
            print("Thank you for playing! Goodbye!")
            break
        
        if user_choice not in choices:
            print("Invalid choice! Please enter R, P, S, or Q.")
            continue
        
        computer_choice = random.choice(choices)
        
        print(f"\nYou chose: {display_choice(user_choice)}")
        print(f"Computer chose: {display_choice(computer_choice)}")
        
        result = determine_winner(user_choice, computer_choice)
        print(result)

if __name__ == "__main__":
    main()
