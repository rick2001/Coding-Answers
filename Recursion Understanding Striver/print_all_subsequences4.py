# storing all the subsequences in an array and printing the array of array;

def subsequence(index, array, emptyarr,totalarr ,count):
    if index == len(array):
        totalarr.append(emptyarr.copy())
        return


    emptyarr.append(array[index])
    subsequence(index+1, array, emptyarr, totalarr,count)

    emptyarr.pop()
    subsequence(index+1, array, emptyarr,totalarr ,count)

    return totalarr  #1st way
index=0
array=[1,2,1]
emparr=[]
totalarr=[]
count=0
print("All the subsequences are-> ",subsequence(index, array, emparr,totalarr ,count))
print(totalarr)   #2nd way


# Output
# All the subsequences are->  [[1, 2, 1], [1, 2], [1, 1], [1], [2, 1], [2], [1], []] #1st way
# [[1, 2, 1], [1, 2], [1, 1], [1], [2, 1], [2], [1], []]   #2nd way
