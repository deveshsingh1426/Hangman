import random

# Define word categories
categories = {
    "Animals": ["elephant", "giraffe", "kangaroo", "dolphin", "penguin"],
    "Programming Languages": ["python", "java", "cplusplus", "javascript", "ruby"],
    "Countries": ["canada", "brazil", "japan", "france", "germany"]
}


def select_random_word(category):
    return random.choice(categories[category])


def display_word(word, guessed):
    return ''.join([letter if guessed[i] else '_' for i, letter in enumerate(word)])


def get_hint(word, guessed):
    for i, letter in enumerate(word):
        if not guessed[i]:
            return f"The letter at position {i + 1} is '{letter}'."
    return "No hints available."


def hangman():
    print("Welcome to Advanced Hangman!")

    # Choose category
    print("Categories:")
    for category in categories:
        print(f"- {category}")
    category = input("Choose a category: ").title()

    if category not in categories:
        print("Invalid category. Exiting.")
        return

    word = select_random_word(category)
    guessed = [False] * len(word)
    max_incorrect_guesses = 8
    incorrect_guesses = 0
    guessed_letters = set()
    hints_used = 0

    print("\nLet's start the game!")
    print(f"Category: {category}")
    print("You have a maximum of 8 incorrect guesses.")

    while incorrect_guesses < max_incorrect_guesses and not all(guessed):
        print(f"\nCurrent word: {display_word(word, guessed)}")
        print(f"Guessed letters: {', '.join(sorted(guessed_letters))}")
        print(f"Incorrect guesses left: {max_incorrect_guesses - incorrect_guesses}")
        print(f"Hints used: {hints_used}")

        choice = input("Enter a letter or type 'hint' for a hint: ").lower()

        if choice == 'hint':
            if hints_used < 1:
                print(get_hint(word, guessed))
                hints_used += 1
            else:
                print("No more hints available.")
            continue

        if not choice.isalpha() or len(choice) != 1:
            print("Invalid input. Please enter a single letter.")
            continue

        if choice in guessed_letters:
            print("You already guessed that letter!")
            continue

        guessed_letters.add(choice)

        if choice in word:
            for i, letter in enumerate(word):
                if letter == choice:
                    guessed[i] = True
        else:
            incorrect_guesses += 1
            print("Incorrect guess!")

    if all(guessed):
        print(f"\nCongratulations! You've guessed the word: {word}")
    else:
        print(f"\nGame over! The word was: {word}")


if __name__ == "__main__":
    hangman()
