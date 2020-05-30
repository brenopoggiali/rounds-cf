from math import factorial
s = input()

can = True
count = 0
for i in s:
	if i == "m" or i == "w":
		can = False
if can:
	count = 0
	repeat = 0
	N, U = False, False
	cnt_repeat = 0
	add = 0
	for i in range(len(s)-1):
		if s[i] == s[i+1] and (s[i] == "u"):
			if U and s[i] == "u":
				cnt_repeat += 1
				repeat += cnt_repeat
				add += cnt_repeat
			else:
				count += 1
			if s[i] == "u": 
				U = True
			else:
				U = False
		else:
			U = False
			cnt_repeat = 0
	cnt_repeat = 0
	for i in range(len(s)-1):
		if s[i] == s[i+1] and (s[i] == "n"):
			if U and s[i] == "n":
				cnt_repeat += 1
				repeat += cnt_repeat
				add += cnt_repeat
			else:
				count += 1

			if s[i] == "n": 
				U = True
			else:
				U = False
		else:
			U = False
			cnt_repeat = 0

	ans = 0
	ans = add
	for i in range(0, count+1):
		ans += factorial(count)//(factorial(i)*factorial(count-i))
	count = ans

print(int(count)%(10**9+7))

