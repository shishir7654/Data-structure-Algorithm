a= [1,3,4,6,2,11,7,0]

for i in range(0,len(a)):
    for j in range(i+1,len(a)):
        if a[j]<a[i]:
            temp = a[j]
            a[j]=a[i]
            a[i]=temp
    print("sorted list are....")
    for i in a:
        print(i)