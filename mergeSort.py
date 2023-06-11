def merge(ar,s,m,e):
    p1 = s
    p2=m+1
    k=0
    ls=[0]*(e-s+1)
    while p1<=m and p2 <=e:
        if ar[p1]<=ar[p2]:
            ls[k]=ar[p1]
            p1 +=1
        else:
            ls[k]=ar[p2]
            p2 +=1
        k +=1

    while(p1<=m):
        ls[k] = ar[p1]
        p1 +=1
        k +=1
    while(p2 <=e):
        ls[k] = ar[p2]
        p2 +=1
        k +=1
    k =0
    for i in range(s,e+1):
        ar[i] = ls[k]
        k +=1
def mergeSort(ar,s,e):
    if(s==e):
        return
    m = (s+e)//2
    mergeSort(ar,s,m)
    mergeSort(ar,m+1,e)
    merge(ar,s,m,e)



ar=[1,3,2,7,4,8,10,0,-11,111,-33]
mergeSort(ar,0,len(ar)-1)
print(ar)
