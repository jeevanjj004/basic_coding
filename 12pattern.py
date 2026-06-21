

def is_palindrome(s):
    a=s.replace(" ","")
    b=a[::-1]

    if b.lower()==a.lower():
        print("True")
    else:
        print("False")
is_palindrome("Nurses Run")