import random

def play_game():
    print("🎮 Welcome to Rock-Paper-Scissors Game!")
    print("Rules: Rock beats Scissors | Scissors beats Paper | Paper beats Rock\n")

    user_score = 0
    computer_score = 0

    while True:
        # Prompt user input
        user_choice = input("Choose Rock, Paper, or Scissors (or 'q' to quit): ").lower()

        if user_choice == 'q':
            print("\n👋 Thanks for playing! Final Scores:")
            print(f"You: {user_score} | Computer: {computer_score}")
            break

        if user_choice not in ["rock", "paper", "scissors"]:
            print("❌ Invalid choice. Please try again.\n")
            continue

        # Computer random choice
        computer_choice = random.choice(["rock", "paper", "scissors"])
        print(f"\n👉 You chose: {user_choice.capitalize()}")
        print(f"🤖 Computer chose: {computer_choice.capitalize()}")

        # Game logic
        if user_choice == computer_choice:
            print("⚖️ It's a Tie!\n")
        elif (
            (user_choice == "rock" and computer_choice == "scissors") or
            (user_choice == "scissors" and computer_choice == "paper") or
            (user_choice == "paper" and computer_choice == "rock")
        ):
            print("🎉 You Win!\n")
            user_score += 1
        else:
            print("😞 You Lose!\n")
            computer_score += 1

        # Display score
        print(f"📊 Current Score -> You: {user_score} | Computer: {computer_score}\n")

# Run the game
play_game()
