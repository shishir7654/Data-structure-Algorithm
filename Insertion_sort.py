a = [10,3,2,5,7,23,44,12]

for k in range(1,8):
    temp = a[k]
    j = k-1

    while j>= 0 and temp<=a[j]:
        a[j+1] = a[j]
        j = j-1
        a[j+1] = temp

print("Printing  sorted array is.....")
for i in a:
    print(i)