#find minimum and maximum element

def find_max_and_min(arr):
    max_val=arr[0]
    min_val=arr[0]

    for i in range(1,len(arr)):
        if arr[i] > max_val:
            max_val = arr[i]

        if arr[i] < min_val:
            min_val = arr[i]
    print(f"max value->{max_val} & min value->{min_val}")

arr=[128, 8,3,4,5,1,0,-1]
find_max_and_min(arr)  # calling function
