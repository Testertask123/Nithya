#print the number within the range 0-6 except 3 & 6
# 0 1 2 3 4 5 6    0 1 2  4 5

print("** 1st way **")
for no in range(7):
    if no== 3 or no ==6:
        continue
    print(no)


print("** 2nd way **")
n1 = 0
while n1< 7:
    if n1!=3 and n1!=6:
        print(n1)
    n1+=1

print("** 3rd way **")

dont = [3,6]
for i in range(7):
    if i not in dont :
        print(i)