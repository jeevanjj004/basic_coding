arr=[0,1,2,3,5]
l=len(arr)
arr1=[]
for i in range(0,l+1):
    arr1.append(i)
    print(arr1)
set1=set(arr)
set2=set(arr1)
diff=set2.difference(set1)
print(diff)




#another optimized version
# expected_sum = n * (n + 1) // 2
# actual_sum = sum(arr)
# missing = expected_sum - actual_sum