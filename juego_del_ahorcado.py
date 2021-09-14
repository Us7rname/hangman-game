import random
import os

def run():
    with open("./word/words.txt", "r", encoding="utf-8") as f:
        words = [word for word in f]
        chosen_word = random.choice(words)
        chosen_word = list(chosen_word)
        chosen_word.remove("\n")
        chosen_word = "".join(chosen_word)
        long = len(chosen_word)
        lives = 6
        def normalize(s):
            replacements = (
            ("á", "a"),
            ("é", "e"),
            ("í", "i"),
            ("ó", "o"),
            ("ú", "u"),
            )
            for a, b in replacements:
                s = s.replace(a, b).replace(a.upper(), b.upper())
            return s
        chosen_word = normalize(chosen_word)

        stages = ['''
         +---+
         |   |
         O   |
        /|\  |
        / \  |
             |
        =========
        ''', '''
         +---+
         |   |
         O   |
        /|\  |
        /    |
             |
        =========
        ''', '''
         +---+
         |   |
         O   |
        /|\  |
             |
             |
        =========
        ''', '''
         +---+
         |   |
         O   |
        /|   |
             |
             |
        =========''', '''
        +---+
        |   |
        O   |
        |   |
            |
            |
        =========
        ''', '''
        +---+
        |   |
        O   |
            |
            |
            |
        =========
        ''', '''
        +---+
        |   |
            |
            |
            |
            |
        =========
        ''']

                       
    
        



        guessed_words = ["_" for letter in range(long)]

        while lives > 0:
            print(chosen_word)
            guess = input("Adivina la palabra antes de que te ahorquen: ")
            assert guess.isnumeric() == False, "Solo se pueden ingresar letras"
            os.system("cls")
            for position in range(long):
                letter_of_chosen_word = chosen_word[position]
                if letter_of_chosen_word == guess:
                    guessed_words[position] = guess
            if guess not in chosen_word:
                print(f"'{guess}' no esta en la palabra")
                lives = (lives - 1)
            if str("".join(guessed_words)) == chosen_word:
                    print("Ganaste")
                    break
            print(" ".join(guessed_words))
            print(f"Te quedan {lives} vidas")
            print(stages[lives])
                
        if str("".join(guessed_words)) != chosen_word:
            print("Perdiste")


      
if __name__ == "__main__":
    run()