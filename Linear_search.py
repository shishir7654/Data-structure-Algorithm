def search(arr,n,x):
    for i in range(0,n):
        if(arr[i]==x):
            return i;
    return -1;

arr=[1,3,4,5,7,8,9];
x=4;
n=len(arr);
result = search(arr,n,x)
if(result==-1):
    print("Element is not found in array")
else:
    print("Element is found at index",result)