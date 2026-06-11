
# the logic is set as second and largest by the first comparison and
#  #loop from 2 if i th element is greater tahn l means largest so current largest move to second and largest update if i th is greater than second update with second
# imp first and second if not interchange order is imp


list2=[6, 8, 5, 4, 7]
length=len(list2)
second=float('-inf')
largest=float('-inf')
if list2[0]>=list2[1]:
    largest=list2[0]
    second=list2[1]

else:
    second=list2[0]
    largest=list2[1]
for i in range(2,length):
    if list2[i]>largest:
        second=largest
        largest=list2[i]
    elif list2[i]>second:
        second=list2[i]
print(second)