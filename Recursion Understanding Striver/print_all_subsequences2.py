# print all the subsequences whose summation is "k";


def subsequence(index, array, newArray,count,k):
    if index == len(array):
        if count==k:
            print(newArray)
        return
    newArray.append(array[index])
    count+=array[index]
    subsequence(index+1, array, newArray,count)


    store = newArray.pop()
    count -= store
    subsequence(index+1, array, newArray,count)


index=0
count=0
k=int(input("Enter the value of k...?"))
arr=[3,2,1]
newArray=[]
subsequence(index,arr,newArray,count,k)

#OUTPUT
# [1, 1]
# [2]
