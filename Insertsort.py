def sort(list):
    for i in range(len(list)-1):
        j=i+1
        key=list[j]
        while i>=0 and list[i]>key:
            list[i+1]=list[i]
            i=i-1
            list[i+1]=key
    return list
list=[2,5,1,4,3]
print(sort(list))