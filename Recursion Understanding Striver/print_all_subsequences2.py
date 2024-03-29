# print all the subsequences whose summation is "k";

# way-1 (This method is not as optimized as 2nd method. because here all the recursions are performed till index reaches length of the array.
def recursion_on_subsequences(index,array,empty_array, final_arr, count,k):
    if index == len(array):
        if count == k:
            final_arr.append(empty_array.copy())
        return

    count+=array[index]
    empty_array.append(array[index])
    recursion_on_subsequences(index+1,array,empty_array, final_arr, count,k)

    count-=array[index]
    empty_array.remove(array[index])
    recursion_on_subsequences(index+1,array,empty_array, final_arr, count,k)


index = 0
array = [1, 2, 1]
empty_array = []
final_arr=[]
count=0
k=int(input("Enter the Target Element-> "))
recursion_on_subsequences(index,array,empty_array, final_arr, count,k)
print(final_arr)

#OUTPUT
#Enter the Target Element-> 2
# [[1, 1], [2]]




# way-2 (This is most optimized than the previous method. Here no of recursion calls are less as a condition is given. so technically the time complexity is less 
# here all the recursions are not preformed if the target condition are not satisfied.
def recursion_on_subsequences(index,array,empty_array, final_arr,target):
    if index == len(array):
        if  target == 0:
            final_arr.append(empty_array.copy())
        return
    if array[index] <=target:
        empty_array.append(array[index])
        recursion_on_subsequences(index + 1, array, empty_array, final_arr, target-array[index])
        empty_array.pop()
    recursion_on_subsequences(index+1,array,empty_array, final_arr,target)

    
    
    
index = 0
array = [1, 2, 1]
empty_array = []
final_arr=[]
# count=0
target = int(input("Enter the Target Element-> "))
recursion_on_subsequences(index,array,empty_array, final_arr, target)
print(final_arr)


#OUTPUT
#Enter the Target Element-> 2
# [[1, 1], [2]]
