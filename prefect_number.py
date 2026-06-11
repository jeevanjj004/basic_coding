def factors(number):
    total=0


#no number has a proper divisor greater than half (except itself)
#SO IF nEEDED WE CAN ALSO USE range(1, number // 2 + 1)


    for i in range(1,number):
        if number%i==0:
            total=total+i
    return total

def perfect_number(number):
    if factors(number)==number:
        print("perfect")
    else:
        print("not perfect")
        
perfect_number(12)