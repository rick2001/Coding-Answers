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
find_nth_primeNumber(7)
