s = "aazbbfccdedd"
st=[]
q=[]
for i in s:
    if i not in st:
        st.append(i)
        q.append(i)
    elif i in q:
        q.remove(i)
print(q[0])

print("USING DICT")
print("/////////////////////////////\n////////////////////////////")
freq={}
for i in s:
    #freq.get(a,0) means return the value of a in freq if exist otherwise 0
    freq[i]=freq.get(i,0)+1


for ch in freq:
    if freq[ch]==1:
        print(ch)
        break