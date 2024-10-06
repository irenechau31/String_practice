# -*- coding: utf-8 -*-
"""
Created on Wed Oct  2 10:51:25 2024

@author: User
"""

# 1. write a function that takes a string as parameter, return true if it’s a valid variable name, false otherwise. You can use keyword module’s  iskeyword() to determine is a string is keyword.
# Starts with letter or underscore
# Contains only alphanumeric or underscore
# Not a keyword
# 	import keyword
# 	keyword.iskeyword(var)   #returns true or false

# 2. write a function that returns the length of a string (without using len() function)
# 3. write a function that counts number of vowels in a string
# 4. write a function that checks if a word is palindrome (a word that reads the same forward and backward)
# #palindrome is a symmetric word around the center
# #refer
import keyword
def string(my_string):
    if keyword.iskeyword(my_string):
        return False
    # Check if the variable starts with a letter or underscore and contains only alphanumeric characters or underscores
    if not (my_string[0].isalpha() or my_string[0]=='_'):
        return False
    for i in my_string[1:]:
        if not (i.isalnum() or i =='_'):
            return False
    return True
print(string("variable1"))  
print(string("1variable"))  
print(string("_variable"))  
print(string("for"))        
    
def string_length(string):
    length=0
    for i in string:
        length+=1
    return length
print(string_length('Irene'))

def count_vowels(string):
    vowels = "aeiouAEIOU"
    count = 0
    for i in string:
        if i in vowels:
            count+=1
    return count
print(count_vowels("hello"))       
print(count_vowels("AEIOU"))       
print(count_vowels("bcdfg"))       

def palindrome(string):
    return string.lower()==string[::-1].lower()
print(palindrome("Level"))
print(palindrome("hello")) 