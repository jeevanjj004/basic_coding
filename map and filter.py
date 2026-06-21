
arr=[1,2,3,344,0]
result=map(lambda x:x*x,arr)
print(list(result))



filter_result=list(filter(lambda x:x%2==0,arr))
print(f" even numbers by filter option {list(filter_result)}")
print((filter_result))