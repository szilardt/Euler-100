"""
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""

import numpy as np
    
def is_positive_prime(num):
    assert 1==num / np.floor(num)
    
    if 2>num : return False
    if 2==num :return True
    
    
    max_num=np.floor(np.sqrt(num) ) + 1
    i=2
    while i< max_num:
        if 0==num%i  :
            return False
        i+=1
    return True


