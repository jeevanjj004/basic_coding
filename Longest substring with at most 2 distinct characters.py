s = "eceba"
left=0
set1=set()
max_len=0
count=0

for right in range(0,(len(s))):
    set1.add(s[right])

    while(len(set1)>2):
        set1.remove(s[left])
        left=left+1
    max_len = (max(max_len,right - left + 1))

print(max_len)




