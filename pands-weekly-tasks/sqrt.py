# squareroot.py
# This program returns the squareroot of an input number 
# Author Ellen McGrory

# This python program using the takes an input number and returns an approximation of the square root of the value. 
# This was achieved using the netwon method of approximation of finding the square root of a value 




# This topic was researched using the code repo on this Github repo URL: https://github.com/ahartz1/approximate-square-root/blob/master/square_root.py
# Backgound to method URL: https://python.pages.doc.ic.ac.uk/2021/lessons/lesson04/04-applied/06-newton.html



def sqrt(num, precision):
    '''
    Finds the square root to a pre-defined minimum precision using Newton's method
    
    num: number to be square rooted
    precision: precision of Newton's method to be given 

    >>>squareroot(25,0.0001)
    >>>The approximate square root of 25 is 5.000000000016778 with a precision of 0.0001
    '''

    # initial guess of half value to have square root completed
    apxroot = num/2
    n = 0
    while abs(num - apxroot**2) > precision:
        if n == 0: 
            print("{} iteration,  guess is {}".format(n+1, round(apxroot,2)))
        else:
            print("{} iterations, guess is {}".format(n+1, round(apxroot,2)))
        apxroot  = (apxroot + num/apxroot)/2
        n += 1
    return apxroot

num=25
precision = 0.0001
a = sqrt(num,precision)
print(f"The approximate square root of {num} is {a} with a precision of {precision}") 
