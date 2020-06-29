from sys import stdin, exit
input = stdin.readline

def i(): return input()
def ii(): return int(input())
def iis(): return map(int, input().split())
def liis():	return list(map(int, input().split()))
def print_array(a): print(" ".join(map(str, a)))

n, m, k = iis()
alice = []
bob = []
both = []
for _ in range(n):
	t, a, b = iis()
	if a == 1 and b == 0:
		alice.append([t, _+1])
	elif a == 0 and b == 1:
		bob.append([t, _+1])
	elif a == 1 and b == 1:
		both.append([t, _+1])
alice = sorted(alice)[::-1]
bob = sorted(bob)[::-1]
both = sorted(both)[::-1]

if len(both)+min()


time = 0
livros = []
while k > 0 and (len(both) != 0 or (len(alice) != 0 and len(bob) != 0)):
	if len(both) and len(alice) and len(bob):
		separado = alice[-1][0]+bob[-1][0]
		junto = both[-1][0]
		if junto < separado:
			time += junto
			livros.append(both[-1][1])
			both.pop()
		else:
			time += separado
			livros.append(alice[-1][1])
			livros.append(bob[-1][1])
			alice.pop()
			bob.pop()
	elif len(both):
		juntos = both.pop()
		time += juntos[0]
		livros.append(juntos[1])
	elif len(alice) and len(bob):
		al = alice.pop()
		bo = bob.pop()
		time += al[0]
		time += bo[0]
		livros.append(al[1])
		livros.append(bo[1])
	else:
		continue
	k -= 1

if k == 0:
	print(time)
	print_array(livros)
else:
	print(-1)
