def selection_sort(a):
    n=len(a)
    for i in range(n):
        min=i
        for j in range(i+1,n):
            if a[min]>a[j]:
                min=j
        a[min],a[i]=a[i],a[min]
    return a
                
l=[5,1,2,7,8,4,9,3,6]
ans=selection_sort(l)
print(*ans)
