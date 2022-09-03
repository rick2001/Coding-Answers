#insertionsort (iterative apprach)
def insertion(arr):
    for i in range(1,len(arr)):
        key=arr[i]
        j=i-1
        # while arr[j] < key and j>=0:  #decending order
        #     arr[j+1]=arr[j]
        #     j-=1
        # arr[j+1]=key

        while arr[j] > key and j>=0:  #ascending order
            arr[j+1]=arr[j]
            j-=1
        arr[j+1]=key
    print(arr)
arr=[5,1,4,2,8]
insertion(arr)
