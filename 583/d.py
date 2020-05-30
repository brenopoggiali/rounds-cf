n, m = map(int, input().split())


count = 0
x_s = {}
y_s = {}
for i in range(1, n+1):
    x_s[i] = 0
for i in range(1, m+1):
    y_s[i] = 0
positions = []
for i in range(1, n+1):
    inp = input()
    for j in range(1, m+1): 
        if inp[j-1] == '#': 
            count += 1
            x_s[i] += 1
            y_s[j] += 1
            positions.append([i,j])
max_x = 0
for i in x_s:
    if x_s[i] != 0:
        max_x += 1

max_y = 0
for i in y_s:
    if y_s[i] != 0:
        max_y += 1

ans = 2
if m-max_y < ans: ans = m-max_y
if n-max_x < ans: ans = n-max_x

if [1,2] in positions:
    if [2,1] in positions: ans = 0
    else: 
        if 1 < ans: ans = 1
elif [2, 1] in positions:
    if 1 < ans: ans = 1
if [n-1, m] in positions:
    if [n, m-1] in positions: ans = 0
    else: 
        if 1 < ans: ans = 1                 
elif [n, m-1] in positions:
    if 1 < ans: ans = 1

if [1,3] in positions:
    if [3.1] in positions and [2,2] in positions:
        ans = 0
    elif [3.1] in positions or [2,2] in positions:
        if 1 > ans: ans = 1
if [n-2, m] in positions or [n, m-2] in positions or [n-1, m-1] in positions:
    if [n, m-2] in positions and [n-1,m-1] in positions and [n-2,m] in positions:
        ans = 0
    if [n, m-2] in positions or [n-1,m-1] in positions:
        if 1 < ans: ans = 1

if ans < 0: ans = 0

print(ans)
