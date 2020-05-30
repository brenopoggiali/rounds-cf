from sys import stdin, exit
from collections import Counter
input = stdin.readline

def i(): return input()
def ii(): return int(input())
def iis(): return map(int, input().split())
def liis():	return list(map(int, input().split()))
def print_array(a): print("".join(map(str, a)))


def get_set_column(sudoku, col):
	cs = set()
	for i in range(len(sudoku)):
		if i == col: continue
		cs.add(sudoku[i][col])
	return cs

def get_set_square(sudoku, pos):
	ss = set()
	i = pos-(pos%3)
	for j in range(i, i+3):
		for k in range(i, i+3):
			if j == k:
				continue
			ss.add(sudoku[j][k])
	return ss


def get_number(sl, sc, ss):
	for i in ss:
		if i in sc:
			if i in sl:
				return i

t = ii()
for _ in range(t):
	sudoku = []
	for i in range(9):
		line = input()
		linea = [c for c in line.strip()]
		sudoku.append(linea)
	
	j = 0
	for i in range(len(sudoku)):
		set_line = set(sudoku[j])
		set_line.discard(sudoku[j][i])
		set_column = get_set_column(sudoku, i)
		set_square = get_set_square(sudoku, i)
		found = get_number(set_line, set_column, set_square)
		sudoku[j][i] = found
		j += 3
		if j > 8:
			j = (j%9)+1
	
	for i in sudoku:
		print_array(i)
