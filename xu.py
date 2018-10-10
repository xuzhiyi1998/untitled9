def Merge(left,right):#将各个子列表排序插入新列表中
    a=[]
    i=j=0
    while i<len(left) and j<len(right):
        if left[i]<right[j]:
            a.append(left[i])
            i=i+1
        else :
            a.append(right[j])
            j=j+1
    a+=(left[i:])#插入剩余的列表元素
    a+=(right[j:])
    return a
def Mergesort(list):#将列表拆分并最后合并
    if len(list)<=1:
        return list
    mid=int(len(list)/2)
    left=Mergesort(list[:mid])
    right=Mergesort(list[mid:])
    Merge(left,right)
    return Merge(left,right)
b=[5,4,3,6,7,8,9]
Mergesort(b)