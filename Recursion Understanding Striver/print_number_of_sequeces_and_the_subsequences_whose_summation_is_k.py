# print number of sequeces + the subsequences whose_summation is k

def subsequence(index, array, emptyarr, count):
    if index == len(array):
        if count ==2:
            print(emptyarr)
            return 1
        else:
            return 0

    count += array[index]
    emptyarr.append(array[index])
    left = subsequence(index+1, array, emptyarr, count)

    count -= array[index]
    emptyarr.pop()
    right = subsequence(index+1, array, emptyarr, count)

    return left+right



index=0
array=[1,2,1]
emparr=[]
count=0
print(subsequence(index, array, emparr, count))

# OUTPUT
# [1,1] ....all the subsequences
# [2]
# 2     ->total no of subsequences
