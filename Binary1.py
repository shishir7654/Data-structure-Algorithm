def binarySearch(arr,beg, end, item):
    if end>=beg:
        mid = int((beg+end)/2)
        if arr[mid]==item:
            return mid+1

        elif arr[mid]<item:
            return binarySearch(arr,mid+1,end,item)
        else:
            return binarySearch(arr,beg,mid-1,item)
    return-1

arr = []
item = int(input("Enter the Array which you find the element "))

location = -1;   
location = binarySearch(arr,item);  
if location != -1:   
    print("Item found at location %d" %(location))  
else:   
    print("Item not found")   