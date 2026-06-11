arr = [-2, -1, -5]
k = 3

curr_sum = 0
pre_sum = float("-inf")

l = 0
r = k

# STEP 1: Build first window of size k
for j in range(0, k):
    curr_sum = arr[j] + curr_sum   # add first k elements

# STEP 2: Initialize best answer with first window
if pre_sum < curr_sum:
    pre_sum = curr_sum

i = 3

# STEP 3: Slide the window until end of array
while i < len(arr):

    # STEP 4: Remove left element of previous window
    curr_sum = curr_sum - arr[l]

    # STEP 5: Add new right element into window
    curr_sum = curr_sum + arr[r]

    # STEP 6: Move window forward
    l = l + 1
    r = r + 1

    # STEP 7: Update best answer
    if pre_sum < curr_sum:
        pre_sum = curr_sum

    i = i + 1

# STEP 8: Print final result
print(pre_sum)