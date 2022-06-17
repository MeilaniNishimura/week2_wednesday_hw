import random
# random.choice(listname)

# possible words
word_choices=["indiana", "flamingo", "software", "clocks", "emerald", "diamond", "leaves", "summer", "gloomy", "september"]

print("Hello! Welcome to hangman. A word has randomly been selected for you to guess. The number of underscores below is the number of letters in the word. If you guess an incorrect letter 7 times, you lose the game. Good luck!")

word = random.choice(word_choices)
print(len(word) * " _ ")
word_dashes= ["_" for i in word]

# begin guessing

incorrect_letters=[]
while len(incorrect_letters) < 7:
    letter_choice=(input("What letter would you like to guess?")).lower()
    if letter_choice in word:
        for idx in range(len(word)):
            if letter_choice == word[idx]:
                word_dashes[idx] = letter_choice
                print(word_dashes)
    else:
        incorrect_letters.append(letter_choice)
    if "_" not in word_dashes:
        print("Congratulations! You beat the game.")
    if (len(incorrect_letters)) >= 7:
        print("Sorry, you lose. This is the corret word." + word)   



