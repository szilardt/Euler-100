"""
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""

import numpy as np

def is_prime(num):
    i=3
    max_num=np.floor(np.sqrt(num) ) + 1
    print(str(num))
    print(str(max_num))
    while i< max_num:
        if 0==num%i  :
            return False
    return True

def find_primes(last_prime=2,to_max):
    upper= np.sqrt(to_max)
    while last_prime < upper:
        if (0==to_max%last_prime): return last_prime
        else:
                last_prime += 1
