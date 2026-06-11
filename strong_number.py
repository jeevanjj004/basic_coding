#145 → 1! + 4! + 5! = 145 ========>strong number

def factorial(num):
    fact=1
    
    if num==1 or num==0:
        return 1
    else:
        fact=num*factorial(num-1)
        return fact
def strong_number(number):
    rem=0
    sum=0
    while number>0:
        rem=number%10
        fact=factorial(rem)
        sum=sum+fact
        number=number//10
    return sum
print(factorial(3))
print(strong_number(145))