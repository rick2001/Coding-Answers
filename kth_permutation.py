def kthPermutation(n,k):
    fact = 1
    aray=[]
    for i in range(1,n):
        fact = fact * i
        aray.append(i)
    aray.append(n)
    k=k-1
    strng="" #this is where we will concatinate
    while(True):
        strng = strng + str(aray[k//fact])
        aray.remove(aray[k//fact])  #remove function takes value
        if len(aray) == 0:
            break
        k = k % fact #16%6 = 4 then 4%2 = 0 then 0%1 = 0
        fact = fact // len(aray)  # it will give us the next factorial
                              # started with 3! then it will give 2! then 1! and so on...
        # print(fact)

    return strng


n = 4 #total no of Array
k = 17 # as we use 0 base indexing we will find 16th sequence
print(kthPermutation(n,k))
