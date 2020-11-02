#iterative approach
def ternary_search_iterative(l,key):
    n=len(l)
    start=0
    end=n-1
    while(start<=end):
        mid1=(start+(end-start))//3
        mid2=(end-(end-start))//3
        if l[mid1]==key:
            return mid1
        elif l[mid2]==key:
            return mid2
        elif l[mid1]<key:
            end=mid1-1
        elif l[mid2]>key:
            start=mid2+1
        else:
            start=mid1+1
            end=mid2-1
    return -1

def ternary_search_recursive(l,key,start,end):
    if start>end:
        return -1
    else:
        mid1=(start+(end-start))//3
        mid2=(end-(end-start))//3
        if l[mid1]==key:
            return mid1
        elif l[mid2]==key:
            return mid2
        elif l[mid1]<key:
            return ternary_search_recursive(l,key,start,mid1-1)
        elif l[mid2]>key:
            return ternary_search_recursive(l,key,mid2+1,end)
        else:
            return ternary_search_recursive(l,key,mid1+1,mid2-1)

l=[1,2,3,4,5,6,7,8,9]
k=3
ans1=ternary_search_iterative(l,k)
print(ans1)
ans2=ternary_search_recursive(l,k,0,len(l)-1)
print(ans2)
