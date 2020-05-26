"""
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""

import numpy as np

num = input("Please enter your number: ")    
num = int(num) # this will block anything which is not integer

while num<2:
    num = input("Please enter your number: ")    
    num = int(num)



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
    
    
    primes_list=[]
    factors_list=[]
    
    max_num= np.floor(num /2)+1
    i=2
    while i< max_num:
        if 0==num %i : 
            if is_positive_prime(i): primes_list.append(i)
            else: factors_list.append(i)
        i+=1            
    
    
    if ( len(factors_list)==0 and len(primes_list)==0 ): 
        print('Congrats! You just have found a real prime number!')
        print(str(num)+ ' is prime')
    elif len(primes_list)==0 :
        print('There are no prime factors of:'+ str(num))
        print('The non-prime factors of ' + str(num) + ' are:')
        print(factors_list)
    else: 
        print('Prime factors of ' + str(num) + ' are:') 
        print(primes_list)
        print('Non-prime factors of ' + str(num) + ' are:') 
        print(factors_list)


list_primes(num)





