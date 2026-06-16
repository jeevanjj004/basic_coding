s="programming"
print(set(s))
s_new=""

print("without set")
for i in s:
    if i not in s_new:
        s_new=s_new+i
print(s_new)