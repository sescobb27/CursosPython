#!/usr/bin/env python3.3
def is_palindrome(str):
	return reverse(str) == str

def reverse(str):
	rev = ''

	for char in str:
		rev = char + rev

	return rev

def is_palindrome_v2(str):
	n = len(str)
	return 	str[:n//2] == reverse(str[n - n // 2:])

n = input("type the word:\n")
while len(n) > 0:
	print("is_palindrome",is_palindrome(n))
	print("is_palindrome_v2",is_palindrome_v2(n))
	n = input("type the word:\n")
# print(is_palindrome('noon'))
# print(is_palindrome('racecar'))
# print(is_palindrome('dented'))
# print('version 2')
# print(is_palindrome_v2('noon'))
# print(is_palindrome_v2('racecar'))
# print(is_palindrome_v2('dented'))