words = ["python", "hangman", "internship", "developer", "keyboard"]
max_wrong = 6


def play():
    word = random.choice(words)
    guessed = set()
    wrong = 0

    print("=== hangman game ===")
    print(f"Guess the word! You have {max_wrong} incorrect guesses allowed.\n")

    while wrong < max_wrong:
        display = "".join(letter if letter in guessed else "_" for letter in word)
        print("word: " + " ".join(display))
        print(f"wrong guesses: {wrong}/{max_wrong}")

        if "_" not in display:
            print("\n🎉 You won! The word was:", word)
            return

        guess = input("Guess a letter: ").lower().strip()

        if len(guess) != 1 or not guess.isalpha():
            print("please enter a single letter.\n")
            continue
        if guess in guessed:
            print("you already guessed that letter.\n")
            continue

        guessed.add(guess)
        if guess not in word:
            wrong += 1
            print("❌ incorrect!\n")
        else:
            print("✅ correct!\n")

    print(f"\n💀 You lost! The word was: {word}")
if __name__ == "__main__":
    play()