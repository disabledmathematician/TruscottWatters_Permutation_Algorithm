def perm_three(L, s1, s2, s3):
	lists = []
	e1, e2, e3 = L[s1], L[s2], L[s3]
	
# I love you Dad Mark William Watters. We have another 20 years ahead of us.

def charles():
	L = [1, 2, 3, 4]
	n = 0
	count = len(L) - 3
	lists = []
	for x in range(0, len(L)):
		L[n], L[x] = L[x], L[n]
		lists.append((L.copy(), x))
		print(L)
		L[n], L[x] = L[x], L[n]
	print(lists)
	for x in lists:
		print(x[0])
		for n in range(len(x[0])):
#			print(n)
			if n != x[1]:
				print(x[0][n])
charles()
