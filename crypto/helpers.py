""" Helper functions for caesar.py and vigenere.py """
__dueDate__ = "5/14/2017"

import string

def alphabet_position(letter):
	""" Receives a letter, returns 0-based numerical position of that letter. """
	letter = letter.lower()
	alphabet = string.ascii_lowercase
	return alphabet.find(letter)

def rotate_character(char, rot):
	""" Receives a character and an integer to rotate char to the right. Keeps capitalization. """
	if char not in string.ascii_letters:
		return char
	alphabet = string.ascii_lowercase
	idx = (alphabet_position(char) + rot) % len(alphabet)
	if char in string.ascii_uppercase:
		return alphabet[idx].upper()
	return alphabet[idx]
	