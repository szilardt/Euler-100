"""
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""

import numpy as np


checkbit= False# this will block anything which is not integer

while not(checkbit):
    try:
        num = input("Please enter your number: ")    
        num = int(num)
        checkbit= True
    except : print('Please enter a real integer higher than 1!')



def is_positive_prime(num):
    
    if 2>num : return False
    if 2==num :return True
    if 3==num : return True
    
    max_num=np.floor(np.sqrt(num) ) + 1
    i=2
    while i< max_num:
        if 0==num%i  :
            return False
        i+=1
    return True

def list_primes(num):
    assert (np.floor(num) == num or 2>num)
    
    primes_max=0
    factors_list=[]
    
    i=int(np.floor(num /2))
    while i> 1:
        if 0==num %i : 
            if is_positive_prime(i):                 
                primes_max=(i)
                i=2
            else: factors_list.append(i)
        i-=1            
    
    if ( len(factors_list)==0 and primes_max==0 ): 
        print('Congrats! You just have found a real prime number!')
        print(str(num)+ ' is prime')
    
    elif len(factors_list)==0: 
        print('There are no non-prime factors between ' + str(num) + ' and '+ str(primes_max))
        print('Highest prime factor of ' + str(num) + ' is:') 
        print(primes_max)
    
    else: 
        print('Highest prime factor of ' + str(num) + ' is:') 
        print(primes_max)
        print('Non-prime factors between ' + str(num) + ' and '+ str(primes_max) + ' are:') 
        print(factors_list)


list_primes(num)





