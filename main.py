#!/usr/bin/env python3

# @author Mohamed Amin Boubaker
# @see    https://www.geeksforgeeks.org/generate-passwords-given-character-set

import sys

# Python3 program to
# generate all passwords
# for given characters

# Recursive helper function,
# adds/removes characters
# until len is reached
def generate(arr, i, s, len):

	# base case
	if (i == 0): # when len has
				# been reached

		# print it out
		print(s)
		return

	# iterate through the array
	for j in range(0, len):

		# Create new string with
		# next character Call
		# generate again until
		# string has reached its len
		appended = s + arr[j]
		generate(arr, i - 1, appended, len)

	return

# function to generate
# all possible passwords
def crack(arr, len):

	# call for all required lengths
	for i in range(1 , len + 1):
		generate(arr, i, "", len)

# Driver Code
arr = list(sys.argv)
arr.pop(0)
len = len(arr)
crack(arr, len)

# This code is contributed by Smita.
