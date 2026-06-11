list1=[1,765,3,98]
largest=list1[0]
length=len(list1)
print(length)

for i in range(0,length):
    if list1[i]>largest:
        largest=list1[i]
    
print(largest)
