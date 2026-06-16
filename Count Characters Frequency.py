from collections import Counter
s="banana"
print(Counter(s))


print("without counter")
d={}
for i in range(0,len(s)):
    if s[i] not in d:
        d[s[i]]=1
    else:
        d[s[i]]=d[s[i]]+1
print(d)

