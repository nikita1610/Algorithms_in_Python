def quick(a,start,end):
    i=(start-1)
    pivot=a[end]
    for j in range(start,end):
        if a[j]<pivot:
            i=i+1
            a[j],a[i]=a[i],a[j]
    a[i+1],a[end]=a[end],a[i+1]
    index=i+1
    return index
        


def quick_sort(a,start,end):
   if start < end :
       index=quick(a,start,end)
       quick_sort(a,start,index-1)
       quick_sort(a,index+1,end)
       
                
l=[5,1,2,7,8,4,9,3,6]
n=len(l)
quick_sort(l,0,n-1)
print(*l)
