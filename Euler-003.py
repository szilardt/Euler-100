"""
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""

import numpy as np

def is_prime(num):
    i=0
    max_num=np.floor(np.sqrt(num) + 1)
    while i< max_num

def find_primes(last_prime=2,to_max):
    upper= np.sqrt(to_max)
    while last_prime < upper:
        if (0==to_max%last_prime): return last_prime
        else:
                last_prime += 1
