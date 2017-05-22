""" Caesar Cipher implementation """
__dueDate__ = "5/14/2017"

from helpers import alphabet_position, rotate_character
from sys import argv, exit

def encrypt(text, rot):
	""" Caesar cipher requires a message and a rotation amount. """
	return "".join(map(lambda x: rotate_character(x, rot), text))

def main():
	""" Print and input statements for user to run program from the terminal. """
	if len(argv) < 2 or not argv[1].isdigit():
		# User can specify rotation number on the command-line while typing the program command.
		print("usage: python caesar.py n")
		exit()
	msg = input("Type a message:\n")

	rotate = argv[1]
	print(encrypt(msg, int(rotate)))

if __name__ == "__main__":
	main()
