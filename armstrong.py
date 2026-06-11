num=153
dup_num=num
total=0
tem=0
while num>0:
    rem=num%10
    tem=rem*rem*rem
    total=total+tem

    num=num//10
if dup_num==total:
    print("armstrong")
else:
    print("not armstrong")