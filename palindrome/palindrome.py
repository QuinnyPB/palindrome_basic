# This small program checks if a word from a given source is 
# Palindrome (can be read exactly the same from front or back)
# Author: Quinn Bruckmann
# Date: 11/01/2022
import math

def isPalindrome(word):
  # loops through word (halfway only)
  for index in range(math.ceil(len(word)/2)):
    # acounts for 0 and -1 indexing in python 
    if word[index] == word[-(index+1)]:
      continue
    else:
      return False  #is not palindrome
    # end of loop
  return True       #is palindorme


#Continuosly obtains a word from user input, displays existence of palindrome property
while True:
  user_word = input("Please enter a word: ")
  if isPalindrome(user_word):
    print(user_word+" is Palindrome!")
  else:
    print(user_word+" is not Palindrome!")
