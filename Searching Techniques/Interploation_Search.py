#iterative approach
def interpolation_search_iterative(l,key):
    n=len(l)-1
    start=0
    end=n-1
    if key < l[start] or key > l[end]:
        return -1
    else:
        while(start<=end):
            index=start+((key-l[start])*(end-start))//(l[end]-l[start])
            if l[index]==key:
                return index
            elif l[index]>key:
                end=index-1
            else:
                start=index+1
    return -1
#recursive approach
def interpolation_search_recursive(l,key,start,end):
    if  key < l[start] or key > l[end]:
        return -1
    if start>end:
        return -1
    else:
        index=start+((key-l[start])*(end-start))//(l[end]-l[start])
        if l[index]==key:
            return index
        elif l[index]>key:
            return interpolation_search_recursive(l,key,start,index-1)
        else:
            return interpolation_search_recursive(l,key,index+1,end)
   

l=[1,2,3,4,5,6,7,8,9]
k=31
ans1=interpolation_search_iterative(l,k)
print(ans1)
ans2=interpolation_search_recursive(l,k,0,len(l)-1)
print(ans2)
