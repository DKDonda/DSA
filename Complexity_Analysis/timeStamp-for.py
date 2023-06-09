'''
    This is to show that time of the system depends on its mood. Run on 
    for several times on terminal and see the difference in each time.
    
    Also compare the time with timeStamp-while.py and see the difference.
    
    This is why we use the Big-Oh notation.
'''
import time
time.time()

timeStamp1 = time.time()
### start the program
number = 100
sum = 0

for i in range(1, number + 1):
    sum += i
### finish the program
timeStamp2 = time.time()

print(sum)
print(timeStamp2-timeStamp1)