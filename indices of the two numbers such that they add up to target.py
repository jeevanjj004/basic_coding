num = [4, 1, 2]
target=8
flag=0
l=len(num)
if l<2:
    print("atleast 2 element needed")
else:

    for i in range(0,l):
        for j in range(0,l):

            if target==(num[i]+num[j]):
                flag=1
                break
            else:
                flag=0
if  flag:
    print(j,i)
else:
    print("no number equal to target")
            
