# num=153
# dup_num=num
# total=0
# tem=0
# while num>0:
#     rem=num%10
#     tem=rem*rem*rem
#     total=total+tem

#     num=num//10
# if dup_num==total:
#     print("armstrong")
# else:
#     print("not armstrong")





num=153
rem=0
sum=0
dup_num=num
while num>0:
    rem=num%10
    rem=rem*rem*rem
    sum=sum+rem
    num=num//10
if (dup_num==sum):
    print("armstrome")
else:
    print("not")