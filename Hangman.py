
word_list = ["apples", "carrots", "oranges", "pineapples", "banana", "pear", "watermelon"]
import random

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

chosen_word = random.choice(word_list)
display = []
for letter in chosen_word:
    display += "_"
    #print(display)

#input iteration
end_of_game = False
lives = 6
while not end_of_game:
    guess = input("Guess a letter: ").lower()

    #print(f"the solution is {chosen_word}")
    #equating input to letters in the word and replacing them
    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
    print(display)
    #losing cause incorrect input         
    if guess not in chosen_word:
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose, Game over")

    #winning cause all spaces has been filled
    if '_' not in display:
        end_of_game = True
        print("You win") 

    print(stages[lives])

    