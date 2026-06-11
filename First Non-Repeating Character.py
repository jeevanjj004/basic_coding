from collections import Counter

string = "aabbccddeeww"

count = Counter(string)

found = False

for ch in string:
    if count[ch] == 1:
        print(ch)
        found = True
        break

if not found:
    print("no non repeating")