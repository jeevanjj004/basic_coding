# words=['h','e','l','l','o']
# length=len(words)
# j=0
# count=[]
# for i in range(0,length):
#     count.append(int(0))

# for i in range(0,length):
#     for j in range(0,length):
#         if words[i]==words[j]:
#             count[i]=count[i]+1
# for i in range(0,length):
#     print(words[i],count[i])

# above out is 
# h 1
# e 1
# l 2
# l 2
# o 1
# l repetting 



words="banana"
freq={}
for ch in words:
    if ch in freq:
        freq[ch]=freq[ch]+1
    else:
        freq[ch]=1
print(freq)