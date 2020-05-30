s = input()

def is_palindrome(s1, s2):
	eh = True
	for i in range(len(s1)//2+1):
		if s1[i] != s2[m-i-1]:
			eh = False
			break
	return eh

def is_palindrome_alone(s1):
	eh = True
	for i in range(len(s1)//2+1):
		if s1[i] != s1[len(s1)-i-1]:
			eh = False
			break
	return eh

print(is_palindrome_alone(s))
