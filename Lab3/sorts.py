def bubble(lst):
    for i in range(len(lst)):
        for j in range(len(lst)-i-1):
            if lst[j]>lst[j+1]:
                lst[j],lst[j+1]=lst[j+1],lst[j]
                

def selection(lst):
    for i in range(0,len(lst)):
        m=i
        for j in range(i+1,len(lst)):
            if lst[j]<lst[m]:
                m=j
        lst[i],lst[m]=lst[m],lst[i]
        
def merge(a,b):
    c=[]
    while len(a)!=0 and len(b)!=0:
        if a[0] < b[0]:
            c.append(a[0])
            a=a[1:]
        else:
            c.append(b[0])
            b=b[1:]
    if len(a)==0:
        c+=b
    else:
        c+=a
    return c
    
def mergesort(lst):
    if len(lst)==0 or len(lst)==1:
        return lst
    else:
        middle=len(lst)//2
        a=mergesort(lst[:middle])
        b=mergesort(lst[middle:])
        return merge(a,b)
    
def partition(lst,lo,hi):
    pivot=lst[hi]
    i=lo-1
    for j in range(lo,hi-1):
        if lst[j] < pivot:
            i+=1
            lst[i],lst[j]=lst[j],lst[i]
    lst[i+1],lst[hi]=lst[hi],lst[i+1]
    return i+1

def quick(lst,lo,hi):
    if lo<hi:
        p=partition(lst,lo,hi)
        quick(lst,lo,p-1)
        quick(lst,p+1,hi)

def quicksort(lst):
    quick(lst,0,len(lst)-1)
