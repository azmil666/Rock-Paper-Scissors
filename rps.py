import random
choices = {
    "rock": "🪨",
    "paper": "📄",
    "scissors": "✂️",
    "lizard": "🦎",
    "spock": "🖖"
}
rules = {
    "rock": ["scissors", "lizard"],
    "paper": ["rock", "spock"],
    "scissors": ["paper", "lizard"],
    "lizard": ["spock", "paper"],
    "spock": ["scissors", "rock"]
}

def get_computer_choice():
    return random.choice(list(choices.keys()))

def determine_winner(player, computer):
    if player == computer:
        return "It's a tie! 🤝"
    elif computer in rules[player]:
        return "You won! 🎉"
    else:
        return "You lost 💀"

def main():
    print("🎮 Welcome to Rock Paper Scissors Lizard Spock! 🎮")
    print("Choices: rock 🪨, paper 📄, scissors ✂️, lizard 🦎, spock 🖖")

    while True:
        player_choice = input("\nEnter your choice: ").lower().strip()
        if player_choice not in choices:
            print("❌ Invalid choice. Try again.")
            continue

        computer_choice = get_computer_choice()

        print(f"\nYou chose: {choices[player_choice]} ({player_choice})")
        print(f"Computer chose: {choices[computer_choice]} ({computer_choice})")

        result = determine_winner(player_choice, computer_choice)
        print(result)

        again = input("\nPlay again? (y/n): ").lower()
        if again != "y":
            print("Thanks for playing! 👋")
            break

if __name__ == "__main__":
    main()
