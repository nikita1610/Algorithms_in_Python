def insertion_sort(a):
    n=len(a)
    for i in range(1,n):
        ele=a[i]
        j=i-1
        while j>=0 and ele < a[j]:
            a[j+1]=a[j]
            j-=1
        a[j+1]=ele
    return a

l=[5,1,2,7,8,4,9,3,6]
ans=insertion_sort(l)
print(*ans)
