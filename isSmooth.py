def isSmooth(arr):
    if len(arr)%2==0:
        mid=arr[len(arr)/2-1]+arr[len(arr)/2]
    else:
        mid=arr[len(arr)/2]
    return arr[0]==arr[len(arr)-1]==mid 
