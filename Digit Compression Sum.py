# You are given a number N.

# You must:

# Extract digits
# Ignore all zeros
# Multiply remaining digits together
# Print the result




num=105204
product=1
rem=0
while num>0:
    rem=num%10
    if rem!=0:
        product=product*rem
    num=num//10
print(product)