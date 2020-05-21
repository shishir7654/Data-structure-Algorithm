arr = [10,20,3,4,5,6,7,8,19];
item = int(input("Enter the item you want to print"));
for i in range(0,len(arr)):
    if arr[i]==item:
        flag = i+1;
        break;
    else:
        flag = 0;
if flag!=0:
    print("item found at loc %d" %(flag));
else:
    print("item not found");