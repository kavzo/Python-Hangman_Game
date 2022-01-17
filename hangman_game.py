import random
from words import word_list

def get_word():
    word = random.choice(word_list)
    return word.upper()

def play(word):
    full_word = "_ " * len(word)
    guessed = False
    guessed_letter = []
    guessed_word = []
    attempts = 6
    print("Lets play hangman")
    print(display_hangman(attempts))
    print(full_word)
    print("\n")
    while not guessed and attempts > 0:
        guess = input("Please guess a letter or word\n").upper()
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letter:
                print("You already guessed the letter", guess)
            elif guess not in word:
                print(guess, "is not in the word.")
                attempts -= 1
                guessed_letter.append(guess)
            else:
                print("Good job,",guess," is in the word")
                guessed_letter.append(guess)
                word_as_list = list(full_word)
                index = [i for i, letter in enumerate(word) if letter == guess]
                for x in index:
                    word_as_list[x] = guess
                full_word = "".join(word_as_list)
                if "_" not in full_word:
                    guessed = True
        elif len(guess) == len(word) and guess.isalpha():
            if guess in guessed_word:
                print("You already guess that word", guess)
            elif guess != word:
                print(guess, " is not the word.")
                attempts -= 1
                guessed_word.append(guess)
            else:
                guessed = True
                full_word = word
        else:
            print("Not a valid guess.")
        print(display_hangman(attempts))
        print(full_word)
        print("\n")
    if guessed:
        print("Congrats, you guessed the word! You win!")
    else:
        print("Sorry, you ran out of attempts. The word was "+ word + " Maybe next time")

            
def display_hangman(attempts):
    stages = [  # final state: head, torso, both arms, and both legs
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                """,
                # head, torso, both arms, and one leg
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                """,
                # head, torso, and both arms
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                """,
                # head, torso, and one arm
                """
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                """,
                # head and torso
                """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                """,
                # head
                """
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                """,
                # initial empty state
                """
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                """
    ]
    return stages[attempts]
def main():
    word = get_word()
    play(word)
    while input("Play Again? (Y/N").upper() == "Y":
        word = get_word()
        play(word)
if __name__=='__main__':
    main()