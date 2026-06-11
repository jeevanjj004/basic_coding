
    
string=")("
stack=[]
inavlid=0
if len(string)<2:
    print("invalid")
else:
        
    for i in string:
        if i=='(' or i=='{' or i=='[':
            stack.append(i)
        elif i==')':
            if len(stack)>0:

                if stack[-1]=='(':
                    stack.pop()
                else:
                    inavlid=1
        elif i==']':
            if len(stack)>0:

                if stack[-1]=='[':
                    stack.pop()
                else:
                    inavlid=1
        elif i=='}':
            if len(stack)>0:

                if stack[-1]=='{':
                    stack.pop()
                else:
                    inavlid=1
        
    if len(stack) or inavlid==1:
        print("invalid")
    else:
        print('valid')
        