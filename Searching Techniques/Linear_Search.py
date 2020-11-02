#iterative approach
def linear_search_iterative(l,key):
    n=len(l)
    index=-1
    for i in range(n):
        if l[i]==key:
            index=i
    return index

#recursive approach
def linear_search_recursive(l,key,idx):
    n=len(l)
    if idx>n:
        return -1
    elif l[idx]==key:
        return idx
    else:
        return linear_search_recursive(l,key,idx+1)

l=[5,1,2,7,8,4,9,3,6]
k=3
ans1=linear_search_iterative(l,k)
print(ans1)
ans2=linear_search_recursive(l,k,0)
print(ans2)
