import random

# List of predefined words
words = ["python", "computer", "coding", "student", "project"]

# Select random word
word = random.choice(words)

guessed_letters = []
wrong_guesses = 0
max_attempts = 6

print("================================")
print("      HANGMAN GAME")
print("================================")
print("Guess the hidden word!")

while wrong_guesses < max_attempts:

    display_word = ""

    for letter in word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print("\nWord:", display_word)

    if "_" not in display_word:
        print("\n🎉 Congratulations!")
        print("You guessed the word:", word)
        break

    guess = input("Enter a letter: ").lower()

    if len(guess) != 1 or not guess.isalpha():
        print("Please enter only one alphabet.")
        continue

    if guess in guessed_letters:
        print("You already guessed this letter.")
        continue

    guessed_letters.append(guess)

    if guess in word:
        print("✅ Correct Guess!")
    else:
        wrong_guesses += 1
        remaining = max_attempts - wrong_guesses
        print("❌ Wrong Guess!")
        print("Attempts Remaining:", remaining)

if wrong_guesses == max_attempts:
    print("\n💀 Game Over!")
    print("The correct word was:", word)