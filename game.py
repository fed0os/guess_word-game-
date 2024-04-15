import random


def choose_word():
    with open('words.txt', 'r') as file:
        words = file.readlines()

    return random.choice(words)


def play_game():
    word = choose_word()
    guessed = "_" * len(word)
    guessed_letters = []
    attempts = 6

    print("Lets start plat game 'Guess word'!")
    print("You have: ", attempts, "attempts. The word consists of", len(word), "letters.")

    while attempts > 0 and "_" in guessed:
        print("\nWord:", " ".join(guessed))
        guess = input("Guess the letter or whole word: ").lower()

        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print("You've already tried this letter.")
            elif guess in word:
                print("Right!")
                guessed_letters.append(guess)
                new_guessed = ""
                for i in range(len(word)):
                    if word[i] in guessed_letters:
                        new_guessed += word[i]
                    else:
                        new_guessed += "_"
                guessed = new_guessed
            else:
                print("Wrong.")
                attempts -= 1
        elif len(guess) == len(word) and guess.isalpha():
            if guess == word:
                guessed = word
            else:
                print("Wrong.")
                attempts -= 1
        else:
            print("Invalid input.")

    if "_" not in guessed:
        print("\nCongratulations, you guessed the word -", word + "!")
    else:
        print("\nUnfortunately, you lost. The right word was -", word + ".")
