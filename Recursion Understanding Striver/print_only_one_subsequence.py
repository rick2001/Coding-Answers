#-> WRITE A PROGRAM TO PRINT ONLY ONE SUBSEQUENCE USING RECURSION


def subsequence(index, array, newArray,count):
    if index == len(array):
        if count==2:
            print(newArray)
            return True
        else:
            return False
    newArray.append(array[index])
    count+=array[index]
    if subsequence(index+1, array, newArray,count)==True:
        return True

    store = newArray.pop()
    count -= store
    if subsequence(index+1, array, newArray,count) == True:
        return True

    return False


index=0
count=0
arr=[1,2,1]
newArray=[]
print(subsequence(index,arr,newArray,count))

# OUTPUT
# [1,1]
