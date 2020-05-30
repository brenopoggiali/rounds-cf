n = int(input())
bra = input()

count = 0
for i in bra:
    if i == '(':
        count += 1
    elif i == ')':
        count -= 1
    if count < -1:
        break

if count < -1 or n%2!=0 or count > 0:
    print("No")
else:
    print("Yes")
