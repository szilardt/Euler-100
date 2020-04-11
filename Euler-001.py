'''

this was edited in new branch

second change
It is changed after local git install
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.

'''
a=0;
b=0;
for i in range(0,1000,3):
    a +=i

for i in range(0,1000,5):
    b +=i

print(a)    
print(b)

print("\nSum is: " + str(a+b))
