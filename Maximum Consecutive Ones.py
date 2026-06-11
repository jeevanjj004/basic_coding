num = [1,1,1,0,1]
current=0
largest=0
for i in num:
    if i==1:
        current=current+1
    else:
        if largest<current:
            largest=current
            current=0
print(largest)