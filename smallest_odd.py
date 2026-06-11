num=8124
flag=0
smallest= float('inf')
while num>0:
    em=num%10
    if em%2!=0:
        flag=1
        if smallest>em:
            smallest=em
    
    num=num//10
if flag:
    print(smallest)
else:
    print("-1")            