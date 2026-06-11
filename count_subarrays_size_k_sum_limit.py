arr = [2, 1, 3, 4, 1]
k = 3
j=0
l=0
r=k
count=0
curr_sum=0
prev_sum=float("-inf")
for i in range(0,k):
    curr_sum=curr_sum+arr[i]
if curr_sum>prev_sum:
    prev_sum=curr_sum
    if prev_sum<5 and prev_sum==5:
        count=count+1
while(j<len(arr)):
    curr_sum=curr_sum-arr[l]
    curr_sum=curr_sum+arr[r]
    
    l=l+1
    r=r+1
    j=j+1
    if curr_sum>prev_sum:
        prev_sum=curr_sum
    if prev_sum<5 and prev_sum==5:
        count=count+1
print(count)