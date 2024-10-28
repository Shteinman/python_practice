import math
import string

# Write a function that computes the volume of a sphere given its radius.

def sphere_vol(rad):
    vol = (4/3)*math.pi*(rad**3)
    return vol
print(sphere_vol(2))


# Write a function that checks whether a number is in a given range (inclusive of high and low)

def ran_check(num,low,high):
    return low < num > high

print(ran_check(5,2,7))

# Write a Python function to check whether a string is pangram or not. (Assume the string passed in does not have any punctuation)

# Note : Pangrams are words or sentences containing every letter of the alphabet at least once.
# For example : "The quick brown fox jumps over the lazy dog"

def ispangram(str1,alphabet=string.ascii_lowercase):
    alphaset = set(alphabet)
    str1 = str1.replace(' ','')
    str1 = str1.lower()
    str1=set(str1)
    return str1 == alphaset

print (ispangram("The quick brown fox jumps over the lazy dog"))