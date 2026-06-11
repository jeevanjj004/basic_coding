# words="banana"
# dup=[]
# for ch in words:
#     if ch in dup:
#         print(ch)
#     else:
#         dup.append(ch)




words="banana"
dup=[]
duplicate=[]
for ch in words:
    if ch in dup:
        duplicate.append(ch)
    else:
        dup.append(ch)
print(set(duplicate))