def bubble_sort(a):
    n=len(a)
    for i in range(n):
        for j in range(n-i-1):
            if a[j]>a[j+1]:
                temp=a[j]
                a[j]=a[j+1]
                a[j+1]=temp
    return a

l=[5,1,2,7,8,4,9,3,6]
ans=bubble_sort(l)
print(*ans)
