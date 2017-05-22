""" Vigenere Cipher implementation """
__dueDate__ = "5/14/2017"

from sys import argv, exit
import string
from helpers import alphabet_position, rotate_character

def encrypt(text, key):
	""" Vigenere Cipher uses a word as the encryption key, rather than an integer."""
	# For text = "The crow" and key = "boom":
	# [The crow]
	# [boo mboo]
	# [Uvs osck]
	idx = 0
	key_list = []
	for char in text:
		if char not in string.ascii_letters:
			key_list += [char]
		else:
			key_letter = key[idx]
			key_list += [alphabet_position(key_letter)]
			idx = (idx + 1) % len(key)
	return "".join(map(rotate_character, text, key_list))

def main():
	""" Print and input statements for user to run program from the terminal. """
	if len(argv) < 2 or not argv[1].isalpha():
		# User can specify encryption key on the command-line while typing the program command.
		print("usage: python vigenere.py keyword")
		print("Arguments:")
		print('keyword : The string to be used as a "key" to encrypt your message. Should only contain alphabetic characters-- no numbers or special characters.')
		exit()
	msg = input("Type a message:\n")
	encrypt_key = argv[1]
	print(encrypt(msg, encrypt_key))

if __name__ == "__main__":
	main()
	