import math, timeit

sequence = 1 
currentNum = 1
previous = 0

#0, 1, 1, 2, 3, 5, 8

start = timeit.default_timer(); 

def main():
    while sequence <= 26:
    

        print(str(sequence) + '. ' + str(previous)) 
    
        temp = currentNum + previous 
        if temp > 26: 
            temp = temp % 26 
        previous = currentNum 
        currentNum = temp 

        sequence += 1 



stop = timeit.default_timer()

print(stop - start)
