import random


with open(".\Desktop\college\sowpods.txt","r") as f:
	lines=list(f)

if __name__ == '__main__':
	print("Welcome to hangman!!")
	word = random.choice(lines).upper()
	guessed = "_" * (len(word)-1)
	word = list(word)
	guessed = list(guessed)
	lstGuessed = []
	letter = input("guess letter: ")
	while True:
		if letter.upper() in lstGuessed:
			letter = ''
			print("Already guessed!!")
		elif letter.upper() in word:
			index = word.index(letter.upper())
			guessed[index] = letter.upper()
			word[index] = '_'
		else:
			print(''.join(guessed))
			if letter is not '':
				lstGuessed.append(letter.upper())
			letter = input("guess letter: ")

		if '_' not in guessed:
			print(''.join(guessed))
			print("You won!!")
			break
	