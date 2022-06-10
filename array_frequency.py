# this is how we can find the frequency of a array elements
arr = [10,2,10,1,10,2]
hasmap={}
for i in range(len(arr)):
    if arr[i] in hasmap:
        hasmap[arr[i]] = hasmap[arr[i]] + 1
    else:
        hasmap[arr[i]] = 1
print(hasmap)
