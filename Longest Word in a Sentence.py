s = "I love python programming language"
sp=s.split()
longest=""
for i in sp:
    if len(i)>len(longest):
        longest=i
print(longest)