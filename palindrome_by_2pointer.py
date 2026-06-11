word = "thopmas"

left = 0
right = len(word) - 1

flag = 1  # assume palindrome

while left < right:
    if word[left] != word[right]:
        flag = 0
        break

    left += 1
    right -= 1

if flag:
    print("palindrome")
else:
    print("not palindrome")