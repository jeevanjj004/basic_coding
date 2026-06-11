word = "abcadef"

seen = set()

left = 0
max_len = 0

for right in range(len(word)):

    # handle duplicate
    if word[right] in seen:
        left=+1
    else:
        seen.add(word[right])
        right=+1
    # add current char

    # update max_len