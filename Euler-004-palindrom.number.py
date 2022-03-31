'''
A palindromic number reads the same both ways. 
The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
'''

import  number_class as number

checkbit1=False

while not(checkbit1):
    try:
        print('\nPlease be aware that the digits of factors for palindrom will be deducted from inital entered number')
        n=input('Please enter the  upper limit for palindrom higher than 10: ')
        n=int(n)
        if n>10 : 
            num=number.NUMBER(n)
            checkbit1=True
    except: print('Please enter a positive integer higher than 10!')
    
digits=num.CountDigits()
print('Number: ' + str(num.get_number()))
print('Digits: ' + str(num.CountDigits()))


#deduct the digits for factors

# checkbit2=False
# while not(checkbit2):
    