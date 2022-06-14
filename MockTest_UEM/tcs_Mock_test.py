# Consider the given series: 1, 2, 1, 3, 2, 5, 3, 7, 5, 11, 8, 13, 13, 17... Now write a program to find the Nth term in this series.
#
# Input Format
#
# Nth term only.
#
# Constraints
#
# 1<=N<=100
#
# Output Format
#
# Output term only.
#
# Sample Input 0
#
# 14
# Sample Output 0
#
# 17
# Explanation 0
#
# 14th term of the series is 17.

import sys
def find_nth_primeNumber(number):
    global store
    count = 0
    for i in range(2,sys.maxsize):
        if count == number:
            # print(f"{number}th prime number is->",store)
            return store
            # break
        for j in range(2,i):
            if i%j == 0:
                break
        else:
            # print("prime number-> ",i)
            count = count + 1
            store = i
# find_nth_primeNumber(7)

def fibonacci(n):
     if n == 1 or n==2:
         return 1
     return fibonacci(n-1) + fibonacci(n-2)

def tcs_Mock_question(position):
    # if n is even then it will be found in (n / 2) position in prime sub series * /

    if position%2 == 0:
        print(find_nth_primeNumber(position//2))

        # / * if n is odd nth number in main series will be found at(n / 2 + 1) position in fibonacci sub series
    else:
        print(fibonacci((position//2)+1))

position = int(input("Enter the position->"))
tcs_Mock_question(position)
