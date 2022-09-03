
# iterative approach (ascending order)
def bubblesort(arr):
    for i in range(len(arr)-1):
        for j in range(len(arr)-1-i):
            if arr[j] > arr[j+1]:
                temp = arr[j]
                arr[j]=arr[j+1]
                arr[j+1]=temp
    # print(arr)
    return arr

arr=[5, 1, 4, 2, 8]
# bubblesort(arr)
print(bubblesort(arr))



# recursive approach (ascending order)
def bubblesort(arr,length):

    if length == 1:
        return arr
    for i in range(length-1):
        if arr[i] > arr[i + 1]:
            temp = arr[i]
            arr[i] = arr[i + 1]
            arr[i + 1] = temp
    return bubblesort(arr,length-1)

arr=[5,1,4,2,8]
length=len(arr)
print(bubblesort(arr,length))
