n = int(input())
c1 = list(map(int, input().split()))
c2 = list(map(int, input().split()))
c3 = list(map(int, input().split()))
my_dict = {}
for _ in range(n-1)
	u, v = map(int, input().split())
	if u not in my_dict:
		my_dict[u]=0
	if v not in my_dict:
		my_dict[v]=0
	my_dict[u]+=1
	my_dict[v]+=1
can = True
for _ in my_dict:
	if my_dict[i] > 2:
		can = False
		break

if not can:
	print(-1)
else:
	ans = []
	for _ in my_dict:
		
		ans.append(1)
