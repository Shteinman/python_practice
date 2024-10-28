# python_practice
# LESSER OF TWO EVENS:
# Write a function that returns the lesser of two given numbers if both numbers are even, but returns the greater if one or both numbers are odd
def lesser_of_two_evens(a,b):
    if a%2 == 0 and b%2 == 0:
        return min(a,b)
    else:
        return max(a,b)

# ANIMAL CRACKERS: 
# Write a function takes a two-word string and returns True if both words begin with same letter

#animal_crackers('Levelheaded Llama') #--> True
#animal_crackers('Crazy Kangaroo') #--> False

def animal_crackers(text):
    wordlist = text.split()
    return wordlist[0][0] == wordlist[1][0]


# MAKES TWENTY: 
# Given two integers, return True if the sum of the integers is 20 or if one of the integers is 20. If not, return False


def makes_twenty(n1,n2):
    return int(n1) == 20 or int(n2) == 20 or sum(n1,n2) == 20


# OLD MACDONALD: Write a function that capitalizes the first and fourth letters of a name

def cap_thy_name(name):
    if len(name) >3:
        return name[:3].capitalize() + name[3:].capitalize()
    else:
        return 'Name is too short'
    
# Check
print (cap_thy_name('macdonald'))
# MASTER YODA: Given a sentence, return a sentence with the words reversed
def master_yoda(text):
    return ' '.join(text.split()[::-1]) #the .join uses what between ' ' as the seperator example 'HEREITIS'.join(a,b,c)
def simple_yoda(text):
    stage_one = text.split()
    stage_two = ' '.join(stage_one[::-1])
    return stage_two

#Check Master yoda
print (master_yoda('I\'m your father!'))

# ALMOST THERE: Given an integer n, return True if n is within 10 of either 100 or 200

def my_almost_there(num):
    return (200 - int(num) <= 10 or 100 - int(num) <= 100)

def almost_there(n):
    return ((abs(100 - n) <= 10) or (abs(200 - n) <= 10))

# Given a list of ints, return True if the array contains a 3 next to a 3 somewhere.
def close_threes(nums):
    for i in range(0, len(nums)-1):
        if nums[i] == 3 and (nums[i]+1 == 3):
            return True
        else:
            return False

print (close_threes([3,3,2]))

# PAPER DOLL: Given a string, return a string where for every character in the original there are three characters

def paper_doll(text):
    result = ''
    for char in text:
        result += char * 3
    return result

# BLACKJACK: 
# Given three integers between 1 and 11, if their sum is less than or equal to 21, return their sum. 
# If their sum exceeds 21 and there's an eleven, reduce the total sum by 10. 
# Finally, if the sum (even after adjustment) exceeds 21, return 'BUST'

def blackjack(a,b,c):
    if sum((a,b,c)) <= 21:
        return sum((a,b,c))
    elif sum((a,b,c)) >= 21 and 11 in ((a,b,c)):
        return sum((a,b,c)) - 10
    else:
        return 'BUST'
    
print (blackjack(11,10,9))

# SUMMER OF '69: 
# Return the sum of the numbers in the array, except ignore sections of numbers starting with a 6 and extending to the next 9 (every 6 will be followed by at least one 9). 
# Return 0 for no numbers.

def no_69(arr):
    total = 0
    add = True
    for i in arr:
        while add:
            if i !=6:
                total += i
                break
            else:
                add = False
        while not add:
            if i != 9:
                break
            else:
                add = True
                break
    return total

print(no_69([2, 1, 6, 9, 11]))


# SPY GAME: 
# Write a function that takes in a list of integers and returns True if it contains 007 in order

def spy_game(nums):
    code = [0,0,7,'x']
    
    for num in nums:
        if num == code[0]:
            code.pop(0)   # code.remove(num) also works
       
    return len(code) == 1

print(spy_game([1,0,2,4,0,5,7]))

# COUNT PRIMES: 
# Write a function that returns the number of prime numbers that exist up to and including a given number

def count_primes(num):
    if num < 2:
        return 0
    primes = [2]
    primes_counter = 3
    while primes_counter <= num:
        for i in range(3,primes_counter,2):
            if primes_counter%i == 0:
                primes_counter += 2
                break
            
        else:
            primes.append(primes_counter)
            primes_counter += 2

    print(primes)
    return len(primes)

print(count_primes(66))

def ran_check(num,low,high):
    if num > low and num < high:
        return True
    else:
        return False
print(ran_check(5,2,7))

# Write a Python function that accepts a string and calculates the number of upper case letters and lower case letters.

# Sample String : 'Hello Mr. Rogers, how are you this fine Tuesday?'
# Expected Output : 
# No. of Upper case characters : 4
# No. of Lower case Characters : 33

def up_low(s):
    d={"upper":0, "lower":0}
    for c in s:
        if c.isupper():
            d["upper"]+=1
        elif c.islower():
            d["lower"]+=1
        else:
            pass
    print("Original String : ", s)
    print("No. of Upper case characters : ", d["upper"])
    print("No. of Lower case Characters : ", d["lower"])

print(up_low('Hello Mr. Rogers, how are you this fine Tuesday?'))


def unique_list(lst):
    unq_list=[]
    for a in lst:
        if a not in unq_list:
            unq_list.append(a)
    print('The original list is: ',lst)
    print('The unique list is: ',unq_list)
    print('Another way to do it is:',list(set(lst)))

unique_list([1,1,1,1,2,2,3,3,3,3,4,5])


def palindrome(s):
    #Remove spaces in the string
    s = s.replace(' ','')
    #Check if the string == reversed string
    if s.lower() == s.lower()[::-1]:
        print('This is a palindrome')
    else:
        print('Just a random string')

palindrome('Dogma I am god')