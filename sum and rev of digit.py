num=123
rem=0
rev=0
total=0
while num>0:
    rem=num%10
    num=num//10
    total=total+rem
    rev=rev*10+rem
print(rev)
print("sum ",total)