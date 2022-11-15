
# -> print the number of sequences whose summationn is k....


def subsequence(index, array,count,k):
    if index == len(array):
        if count==k:
            return 1
        else:
            return 0

    count+=array[index]
    l=subsequence(index+1, array,count,k)


    count -= array[index]
    r=subsequence(index+1, array, count,k)

    return l+r


index=0
count=0
k=int(input("Enter the value of k ?"))
arr=[1,1,1]
print(subsequence(index,arr,count,k))


# OUTPUT
# 3
