# print all the subsequences whose summation is "k";


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
