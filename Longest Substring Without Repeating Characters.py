s = "abcabcbb"

left = 0
max_len = 0
set1 = set()

# STEP 1: Expand window using right pointer
for right in range(0, len(s)):

    # STEP 2: If duplicate found, shrink window from left
    while s[right] in set1:
        set1.remove(s[left])   # remove left character from window
        left = left + 1       # move left pointer forward

    else:
        # STEP 3: Add current character after window becomes valid
        set1.add(s[right])

    # STEP 4: Update maximum length of valid window
    max_len = max(max_len, right - left + 1)

# STEP 5: Output result
print(max_len)