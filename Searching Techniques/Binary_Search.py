def binary_search_iterative(l,key):
    n=len(l)
    start=0
    end=n-1
    while(start<=end):
        mid=(start+end)//2
        if l[mid]==key:
            return mid
        elif l[mid]>key:
            end=mid-1
        else:
            start=mid+1
    return -1

def binary_search_recursive(l,start,end,key):
    if start > end:
        return -1
    else:
        mid=(start+end)//2
        if l[mid]==key:
            return mid
        elif l[mid]>key:
            return binary_search_recursive(l,start,mid-1,key)
        else:
            return binary_search_recursive(l,mid+1,end,key)

l=[1,2,3,4,5,6,7,8,9,10]
k=10
ans1=binary_search_iterative(l,k)
print(ans1)
start=0
end=len(l)-1
ans2=binary_search_recursive(l,start,end,k)
print(ans2)
