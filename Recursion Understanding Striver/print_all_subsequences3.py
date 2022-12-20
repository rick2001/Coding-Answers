def subsequence(index, array, emptyarr, count):
    if index == len(array):
        print(emptyarr)
        return 1

    emptyarr.append(array[index])
    left = subsequence(index+1, array, emptyarr, count)

    emptyarr.pop()
    right = subsequence(index+1, array, emptyarr, count)

    return left+right


index=0
array=[1,2,1]
emparr=[]
count=0
print("Total no of sequences-> ", subsequence(index, array, emparr, count))


# Output

# [1, 2, 1]
# [1, 2]
# [1, 1]
# [1]
# [2, 1]
# [2]
# [1]
# []
# Total no of sequences->  8
