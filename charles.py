def perm_two(L):
	lists = []
	lists.append(L.copy())
	e2, e1 = L[1], L[0]
	L[0], L[1] = e2, e1
	lists.append(L.copy())
	print(lists)
	return lists
def perm_three(L, s1, s2, s3):
	lists = []
	e1, e2, e3 = L[s1], L[s2], L[s3]
	lists.append(L.copy())
	L[s2], L[s3] = e3, e2
	lists.append(L.copy())
	L[s2], L[s3] = e2, e3
	L[s1], L[s2] = e2, e1
	lists.append(L.copy())
	L[s2], L[s3] = e3, e1
	lists.append(L.copy())
	L[s1], L[s2], L[s3] = e1, e2, e3
	L[s1], L[s3] = e3, e1
	lists.append(L.copy())
	L[s2], L[s3] = e1, e2
	lists.append(L.copy())
#	L[s2], L[s3] = e3, e2
#	lists.append(L.copy())
#	L[s2], L[s3] = e2, e3
#	L[s1], L[s2] = e2, e1
#	lists.append(L.copy())
#	L[s1], L[s2] = e1, e2
#	L[s2], L[s3] = e3, e2
#	lists.append(L.copy())
#	L[s2], L[s3] = e2, e3
#	L[s1], L[s2] = e1, e2
#	L[s1], L[s3] = e3, e1
#	lists.append(L.copy())
#	L[s2], L[s3] = e1, e2
#	lists.append(L.copy())
	print(lists)
	return lists
# I love you Dad Mark William Watters. We have another 20 years ahead of us.
# IT is my birthday today
# Byron Bay, NSW 2481 Australia
# Most of the inductive case sound. My solution is to swap all n over 3 elements then complete the factorial of three by allowing storage of all n is greater than 3 elements to be swapped to each other place then complete the permutations of three. To be true to infinity it needs to, say, for gamma six, swap the first to all six places, the second element to all five places except where the first is, the third to all four places, and then complete gamma three for all combinatorially plausible, for example in a queue. Inductive definition is that if the factorial of two can be completed, and the factorial of three can, for all swaps, then the factorial swap of infinity can be completed
# Charles Truscott Watters, 12th of January 2024, one day before my 31st birthday in Byron Bay Australia, where I have lived since 1993 with my father Mark and brother Tai.
def charles(L):
	n = 0
	count = len(L) - 3
	nth = L[1]
	lists = []
	for x in range(0, len(L)):
		L[n], L[x] = L[x], L[n]
		lists.append((L.copy(), x))
#		print(L)
		L[n], L[x] = L[x], L[n]
#	print(lists)
	nths = []
	count = 0
	for x in lists:
		for n in range(len(x[0])):
			if x[0][n] == nth:
				nths.append((count, n))
		count += 1
	Indexes = []
	for x in lists:
		print(x[0])
		for n in range(len(x[0])):
#			print(n)
			if n != x[1]:
#				print(x[0][n])
				Indexes.append(n)
#		print(Indexes)
		perm_three(x[0], Indexes[0], Indexes[1], Indexes[2])
		Indexes = []
#	print(nths)
def give_permutation(L):
	if len(L) == 1:
		return L[0]
	elif len(L) == 2:
		return perm_two(L)
	elif len(L) == 3:
		return perm_three(L, 0, 1, 2)
	elif len(L) == 4:
		return charles(L)
	else:
		raise NotImplementedError
def CharlesTruscott():
	L1 = ["Jin Jiao", "Yin Bi"]
	L2 = ["D", "a", "y"]
	L3 = ["Н", "о", "ч"]
	L4 = ["Д", "е", "н"]
	L5 = [2, 4, 8, 1]
	L6 = ["East", "West", "Schism"]
	L7 = [1, 0, 5, 4]
	try:
		for l in [L1, L2, L3, L4, L5]:
			print("The permutations of {} are ".format(l))
			give_permutation(l)
		for l in [L6, L7]:
			print("The permutations of {} are ".format(l))
			give_permutation(l)
	except NotImplementedError as e:
		print("Sorry: {}".format(e))

CharlesTruscott()
""" The permutations of ['Jin Jiao', 'Yin Bi'] are
[['Jin Jiao', 'Yin Bi'], ['Yin Bi', 'Jin Jiao']]
The permutations of ['D', 'a', 'y'] are
[['D', 'a', 'y'], ['D', 'y', 'a'], ['a', 'D', 'y'], ['a', 'y', 'D'], ['y', 'a', 'D'], ['y', 'D', 'a']]
The permutations of ['Н', 'о', 'ч'] are
[['Н', 'о', 'ч'], ['Н', 'ч', 'о'], ['о', 'Н', 'ч'], ['о', 'ч', 'Н'], ['ч', 'о', 'Н'], ['ч', 'Н', 'о']]
The permutations of ['Д', 'е', 'н'] are
[['Д', 'е', 'н'], ['Д', 'н', 'е'], ['е', 'Д', 'н'], ['е', 'н', 'Д'], ['н', 'е', 'Д'], ['н', 'Д', 'е']]
The permutations of [2, 4, 8, 1] are
[2, 4, 8, 1]
[[2, 4, 8, 1], [2, 4, 1, 8], [2, 8, 4, 1], [2, 8, 1, 4], [2, 1, 8, 4], [2, 1, 4, 8]]
[4, 2, 8, 1]
[[4, 2, 8, 1], [4, 2, 1, 8], [8, 2, 4, 1], [8, 2, 1, 4], [1, 2, 8, 4], [1, 2, 4, 8]]
[8, 4, 2, 1]
[[8, 4, 2, 1], [8, 1, 2, 4], [4, 8, 2, 1], [4, 1, 2, 8], [1, 4, 2, 8], [1, 8, 2, 4]]
[1, 4, 8, 2]
[[1, 4, 8, 2], [1, 8, 4, 2], [4, 1, 8, 2], [4, 8, 1, 2], [8, 4, 1, 2], [8, 1, 4, 2]]
The permutations of ['East', 'West', 'Schism'] are
[['East', 'West', 'Schism'], ['East', 'Schism', 'West'], ['West', 'East', 'Schism'], ['West', 'Schism', 'East'], ['Schism', 'West', 'East'], ['Schism', 'East', 'West']]
The permutations of [1, 0, 5, 4] are
[1, 0, 5, 4]
[[1, 0, 5, 4], [1, 0, 4, 5], [1, 5, 0, 4], [1, 5, 4, 0], [1, 4, 5, 0], [1, 4, 0, 5]]
[0, 1, 5, 4]
[[0, 1, 5, 4], [0, 1, 4, 5], [5, 1, 0, 4], [5, 1, 4, 0], [4, 1, 5, 0], [4, 1, 0, 5]]
[5, 0, 1, 4]
[[5, 0, 1, 4], [5, 4, 1, 0], [0, 5, 1, 4], [0, 4, 1, 5], [4, 0, 1, 5], [4, 5, 1, 0]]
[4, 0, 5, 1]
[[4, 0, 5, 1], [4, 5, 0, 1], [0, 4, 5, 1], [0, 5, 4, 1], [5, 0, 4, 1], [5, 4, 0, 1]]

[Program finished]
"""