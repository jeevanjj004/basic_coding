def odd_or_even(number):
    if number % 2==0:
        return 1
    else:
        return 0
num=582437
total=0
while num>0:
    rem=num%10
    if odd_or_even(rem):
        total=total+rem
    num=num//10
print(total)



#reverse the even digit
num = 109870

evens = []

# step 1: collect digits
while num > 0:
    rem = num % 10
    if rem % 2 == 0:
        evens.append(rem)
    num = num // 10

# step 2: reverse to restore original order
evens.reverse()

# step 3: build final number
result = 0
for d in evens:
    result = result * 10 + d

print(result)