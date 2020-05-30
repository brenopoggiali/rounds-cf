from sys import exit

def i(): return input()
def ii(): return int(input())
def iis(): return map(int, input().split())
def liis():	return list(map(int, input().split()))
def print_array(a): print(" ".join(map(str, a)))


def find_subarrays_0(arr, n):
	hash_map = {}
	out = []
	sum1 = 0
	for i in range(n):
		sum1 += arr[i]
		if sum1 == 0:
			out.append((0, i))
		al = []
		if sum1 in hash_map:
			al = hash_map[sum1]
			for it in range(len(al)):
				out.append((al[it]+1, i))
		al.append(i)
		hash_map[sum1] = al
	return out

def count_exclude_subarrays(arr, zeros):
	return 0


n = ii()
a = liis()
all_options = (n*(n+1))//2

zeros = find_subarrays_0(a, n)
count = count_exclude_subarrays(a, zeros)
print(zeros)
print(all_options-count)

