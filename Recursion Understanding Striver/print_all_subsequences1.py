
#-> print all the subquences.
#-> subsequences means either contigious or non-contigious sequences where order is maintained



def subsequence(index, array, newArray):
    if index == len(array):
        print(newArray)
        return
    newArray.append(array[index])
    subsequence(index+1, array, newArray)
    newArray.pop()
    subsequence(index+1, array, newArray)

index=0
count=0
arr=[3,2,1]
newArray=[]
subsequence(index,arr,newArray)

#OUTPUT
# [3, 2, 1]
# [3, 2]
# [3, 1]
# [3]
# [2, 1]
# [2]
# [1]
# []
