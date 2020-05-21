a= [10,9,4,3,1,7,2,88,40]

for i in range(0,len(a)):
    for j in range(i+1,len(a)):
        if a[j]<a[i]:
            temp = a[j]
            a[j]= a[i]
            a[i]=temp

print("Sorting Elements are.....")
for i in a:
    print(i)