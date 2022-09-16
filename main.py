import hangman_words
import random
from hangman_art import logo, stages
#Declare variables
print(logo)
game_is_finished = False
lives = len(stages) - 1

#TODO-1 Fetch words list from hangman_words and create a random word
word_list = hangman_words.word_list
chosen_word = random.choice(word_list)

#TODO-2 Create blank letters.
display = []
for _ in range(len(chosen_word)):
	display += '_'

#TODO-3 Start the game
while not game_is_finished:
	guess = input('Guess a letter: ').lower()

  if guess in display:
    print(f'You have guessed {guess} already')
	for index in range(len(chosen_word)):
		letter = chosen_word[index]
		if guess == letter:
			display[index] = letter

	print(f"{' '.join(display)}")

	if guess not in chosen_word:
		print(
		    f'You guessed `{guess}` letter, that`s not in the word. You lose a life.'
		)
		lives -= 1
		if lives == 0:
			game_is_finished = True
			print('You lose.')

	if not '_' in display:
		game_is_finished = True
		print('You win.')

	print(stages[lives])
