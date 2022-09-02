# find the unique elements from an array using recursion(BackTracking)
# Time Complexity = O(N)
# def unique_elements(array,empty_array,array_length):
#     if (array_length > -1):
#         unique_elements(array,empty_array,array_length-1)
#         if array[array_length] in empty_array:
#             pass
#         else:
#             empty_array.append(array[array_length])
#     return empty_array
# array = [2,2,2,2,2,2,22,2,2,2,2]
# empty_array = []
# array_length = len(array)-1
# print(unique_elements(array,empty_array,array_length))


def unique_elements(array,array_length):
    # stack = []  # using stack
    # for i in range(array_length):
    #     if array[i] in stack:
    #         continue
    #     else:
    #         stack.append(array[i])
    # return stack

    #or
    stack=[]
    top=-1
    for i in range(array_length):
        if top==-1:
            stack.append(array[i])
            top+=1
        else:
            if stack[top]==array[i]:
                continue
            else:
                stack.append(array[i])
    return stack
array = [2,2,2,2,2,2,22,2,24,2,2,2]
array_length = len(array)-1
print(unique_elements(array,array_length))
