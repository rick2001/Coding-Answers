#selection sort (iterative approach)
"""basic rule is find the mminimum element in the array and replace it with the indexs from first to last

approach-> we will consider the 1st element as the minimum element and then compare it with all the elements in the array
and find the minimum element and swap it with 1st index. then again we will consider the 2nd index as the minimum element
and comapre it with whole array and find the second minimum element and swap it with the 2nd index and so on...
"""
def selectionsort(arr):
    for i in range(len(arr)-1):
        indexofmin=i      #for that time only considering only that this is the minimum value index
        for j in range(i+1,len(arr)):
            if arr[j] < arr[indexofmin]:
                indexofmin=j
                
        temp=arr[i]
        arr[i]=arr[indexofmin]
        arr[indexofmin]=temp
    print(arr)

arr=[128,2,5,3,9,5,3]
selectionsort(arr)
