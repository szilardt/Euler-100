'''

If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.

'''
checkbit1=False
while False==checkbit1:
    try:    
        a=input('Enter the first positive integer:')
        a=int(a)
        if a>0: checkbit1=True
    except : print('Positive integer please, try again!')
    
checkbit2=False
while False==checkbit2:
    try:
        b=input('Enter the second number :')
        b=int(b)
        if b>0 :checkbit2=True
    except: print('Positive integer please, try again!')
    
checkbit3=False
while False==checkbit3:
    try:
        c=input('Enter the limit :')
        c=int(c)
        assert c>max(a,b)
        checkbit3=True
    except : print('The limit must be an integer which is higher than any of previously entered numbers')


a_list=[]
b_list=[]
a_sum=0
b_sum=0

for i in range(0,c,a):
    a_list.append(i)
    a_sum +=i

for i in range(0,c,b):
    b_list.append(i)
    b_sum +=i

print('\nSum of first set :' + str(a_sum))    
print('Sum of second set :' + str(b_sum))    
print('Sum of ' + str(a_sum)+ ' and ' + str(b_sum) + ' is: ' + str(a_sum + b_sum))
print('Multiples of a are: ')
print(a_list)

print('Multiples of b are: ')
print(b_list)


print("\nTotal sum of a+b is: " + str(a_sum +b_sum))
