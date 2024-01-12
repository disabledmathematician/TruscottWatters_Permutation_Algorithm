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

	print(lists)
	return lists
# I love you Dad Mark William Watters. We have another 20 years ahead of us.
# IT is my birthday today
# Byron Bay, NSW 2481 Australia

def charles(L):
	n = 0
	count = len(L) - 3 - 1
	nth = L[1]
	lists = []
	subsequent_elems = []
	subs_elems_L = []
	while count > 0:
		e = L[count]
		subsequent_elems.append((e, count))
		subs_elems_L.append(e)
		count -= 1
	print(subsequent_elems)
	count = 0
	for x in range(0, len(L)):
		L[n], L[x] = L[x], L[n]
		lists.append((L.copy(), x))
		print(L)
		L[n], L[x] = L[x], L[n]
	tries = []
	for l in lists:
		for e in subsequent_elems:
			print(l, e)
			if e[1] != l[1]:
				print("Element {}, which is {}, needs to be swapped in {}".format(e[1], e[0], l[0]))
				count = len(L) - 1
				while count > 0:
					if count != l[1] and e[1] != l[1]:
						l[0][e[1]], l[0][count] = l[0][count], l[0][e[1]]
						print(l[0])
						others = []
						for n in range(len(l[0])):
							if l[0][n] in subs_elems_L:
								others.append(n)
						others.append(l[1])
						tries.append((l[0].copy(), others))
						l[0][count], l[0][e[1]] = l[0][e[1]], l[0][count]
						others = []

					count -= 1
				count = 0
	for element in tries:
		print("In the sequence {} the elements which can't be swapped are: ".format(element[0]))
		for n in element[1]:
			print("{} under index {}".format(element[0][n], n))
	print("Then the factorial of three is completed")
# Thank you Ana Bell, Eric Grimson and John Guttag from MIT for teaching me in 6.001x and 6.002x


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
	L = [1, 2, 3, 4, 5, 6, 7]
	charles(L)
#	L1 = ["Jin Jiao", "Yin Bi"]
#	L2 = ["D", "a", "y"]
#	L3 = ["Н", "о", "ч"]
#	L4 = ["Д", "е", "н"]
#	L5 = [2, 4, 8, 1]
#	L6 = ["East", "West", "Schism"]
#	L7 = [1, 0, 5, 4]
#	try:
#		for l in [L1, L2, L3, L4, L5]:
#			print("The permutations of {} are ".format(l))
#			give_permutation(l)
#		for l in [L6, L7]:
#			print("The permutations of {} are ".format(l))
#			give_permutation(l)
#	except NotImplementedError as e:
#		print("Sorry: {}".format(e))

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

"""
[(4, 3), (3, 2), (2, 1)]
[1, 2, 3, 4, 5, 6, 7]
[2, 1, 3, 4, 5, 6, 7]
[3, 2, 1, 4, 5, 6, 7]
[4, 2, 3, 1, 5, 6, 7]
[5, 2, 3, 4, 1, 6, 7]
[6, 2, 3, 4, 5, 1, 7]
[7, 2, 3, 4, 5, 6, 1]
([1, 2, 3, 4, 5, 6, 7], 0) (4, 3)
Element 3, which is 4, needs to be swapped in [1, 2, 3, 4, 5, 6, 7]
[1, 2, 3, 7, 5, 6, 4]
[1, 2, 3, 6, 5, 4, 7]
[1, 2, 3, 5, 4, 6, 7]
[1, 2, 3, 4, 5, 6, 7]
[1, 2, 4, 3, 5, 6, 7]
[1, 4, 3, 2, 5, 6, 7]
([1, 2, 3, 4, 5, 6, 7], 0) (3, 2)
Element 2, which is 3, needs to be swapped in [1, 2, 3, 4, 5, 6, 7]
[1, 2, 7, 4, 5, 6, 3]
[1, 2, 6, 4, 5, 3, 7]
[1, 2, 5, 4, 3, 6, 7]
[1, 2, 4, 3, 5, 6, 7]
[1, 2, 3, 4, 5, 6, 7]
[1, 3, 2, 4, 5, 6, 7]
([1, 2, 3, 4, 5, 6, 7], 0) (2, 1)
Element 1, which is 2, needs to be swapped in [1, 2, 3, 4, 5, 6, 7]
[1, 7, 3, 4, 5, 6, 2]
[1, 6, 3, 4, 5, 2, 7]
[1, 5, 3, 4, 2, 6, 7]
[1, 4, 3, 2, 5, 6, 7]
[1, 3, 2, 4, 5, 6, 7]
[1, 2, 3, 4, 5, 6, 7]
([2, 1, 3, 4, 5, 6, 7], 1) (4, 3)
Element 3, which is 4, needs to be swapped in [2, 1, 3, 4, 5, 6, 7]
[2, 1, 3, 7, 5, 6, 4]
[2, 1, 3, 6, 5, 4, 7]
[2, 1, 3, 5, 4, 6, 7]
[2, 1, 3, 4, 5, 6, 7]
[2, 1, 4, 3, 5, 6, 7]
([2, 1, 3, 4, 5, 6, 7], 1) (3, 2)
Element 2, which is 3, needs to be swapped in [2, 1, 3, 4, 5, 6, 7]
[2, 1, 7, 4, 5, 6, 3]
[2, 1, 6, 4, 5, 3, 7]
[2, 1, 5, 4, 3, 6, 7]
[2, 1, 4, 3, 5, 6, 7]
[2, 1, 3, 4, 5, 6, 7]
([2, 1, 3, 4, 5, 6, 7], 1) (2, 1)
([3, 2, 1, 4, 5, 6, 7], 2) (4, 3)
Element 3, which is 4, needs to be swapped in [3, 2, 1, 4, 5, 6, 7]
[3, 2, 1, 7, 5, 6, 4]
[3, 2, 1, 6, 5, 4, 7]
[3, 2, 1, 5, 4, 6, 7]
[3, 2, 1, 4, 5, 6, 7]
[3, 4, 1, 2, 5, 6, 7]
([3, 2, 1, 4, 5, 6, 7], 2) (3, 2)
([3, 2, 1, 4, 5, 6, 7], 2) (2, 1)
Element 1, which is 2, needs to be swapped in [3, 2, 1, 4, 5, 6, 7]
[3, 7, 1, 4, 5, 6, 2]
[3, 6, 1, 4, 5, 2, 7]
[3, 5, 1, 4, 2, 6, 7]
[3, 4, 1, 2, 5, 6, 7]
[3, 2, 1, 4, 5, 6, 7]
([4, 2, 3, 1, 5, 6, 7], 3) (4, 3)
([4, 2, 3, 1, 5, 6, 7], 3) (3, 2)
Element 2, which is 3, needs to be swapped in [4, 2, 3, 1, 5, 6, 7]
[4, 2, 7, 1, 5, 6, 3]
[4, 2, 6, 1, 5, 3, 7]
[4, 2, 5, 1, 3, 6, 7]
[4, 2, 3, 1, 5, 6, 7]
[4, 3, 2, 1, 5, 6, 7]
([4, 2, 3, 1, 5, 6, 7], 3) (2, 1)
Element 1, which is 2, needs to be swapped in [4, 2, 3, 1, 5, 6, 7]
[4, 7, 3, 1, 5, 6, 2]
[4, 6, 3, 1, 5, 2, 7]
[4, 5, 3, 1, 2, 6, 7]
[4, 3, 2, 1, 5, 6, 7]
[4, 2, 3, 1, 5, 6, 7]
([5, 2, 3, 4, 1, 6, 7], 4) (4, 3)
Element 3, which is 4, needs to be swapped in [5, 2, 3, 4, 1, 6, 7]
[5, 2, 3, 7, 1, 6, 4]
[5, 2, 3, 6, 1, 4, 7]
[5, 2, 3, 4, 1, 6, 7]
[5, 2, 4, 3, 1, 6, 7]
[5, 4, 3, 2, 1, 6, 7]
([5, 2, 3, 4, 1, 6, 7], 4) (3, 2)
Element 2, which is 3, needs to be swapped in [5, 2, 3, 4, 1, 6, 7]
[5, 2, 7, 4, 1, 6, 3]
[5, 2, 6, 4, 1, 3, 7]
[5, 2, 4, 3, 1, 6, 7]
[5, 2, 3, 4, 1, 6, 7]
[5, 3, 2, 4, 1, 6, 7]
([5, 2, 3, 4, 1, 6, 7], 4) (2, 1)
Element 1, which is 2, needs to be swapped in [5, 2, 3, 4, 1, 6, 7]
[5, 7, 3, 4, 1, 6, 2]
[5, 6, 3, 4, 1, 2, 7]
[5, 4, 3, 2, 1, 6, 7]
[5, 3, 2, 4, 1, 6, 7]
[5, 2, 3, 4, 1, 6, 7]
([6, 2, 3, 4, 5, 1, 7], 5) (4, 3)
Element 3, which is 4, needs to be swapped in [6, 2, 3, 4, 5, 1, 7]
[6, 2, 3, 7, 5, 1, 4]
[6, 2, 3, 5, 4, 1, 7]
[6, 2, 3, 4, 5, 1, 7]
[6, 2, 4, 3, 5, 1, 7]
[6, 4, 3, 2, 5, 1, 7]
([6, 2, 3, 4, 5, 1, 7], 5) (3, 2)
Element 2, which is 3, needs to be swapped in [6, 2, 3, 4, 5, 1, 7]
[6, 2, 7, 4, 5, 1, 3]
[6, 2, 5, 4, 3, 1, 7]
[6, 2, 4, 3, 5, 1, 7]
[6, 2, 3, 4, 5, 1, 7]
[6, 3, 2, 4, 5, 1, 7]
([6, 2, 3, 4, 5, 1, 7], 5) (2, 1)
Element 1, which is 2, needs to be swapped in [6, 2, 3, 4, 5, 1, 7]
[6, 7, 3, 4, 5, 1, 2]
[6, 5, 3, 4, 2, 1, 7]
[6, 4, 3, 2, 5, 1, 7]
[6, 3, 2, 4, 5, 1, 7]
[6, 2, 3, 4, 5, 1, 7]
([7, 2, 3, 4, 5, 6, 1], 6) (4, 3)
Element 3, which is 4, needs to be swapped in [7, 2, 3, 4, 5, 6, 1]
[7, 2, 3, 6, 5, 4, 1]
[7, 2, 3, 5, 4, 6, 1]
[7, 2, 3, 4, 5, 6, 1]
[7, 2, 4, 3, 5, 6, 1]
[7, 4, 3, 2, 5, 6, 1]
([7, 2, 3, 4, 5, 6, 1], 6) (3, 2)
Element 2, which is 3, needs to be swapped in [7, 2, 3, 4, 5, 6, 1]
[7, 2, 6, 4, 5, 3, 1]
[7, 2, 5, 4, 3, 6, 1]
[7, 2, 4, 3, 5, 6, 1]
[7, 2, 3, 4, 5, 6, 1]
[7, 3, 2, 4, 5, 6, 1]
([7, 2, 3, 4, 5, 6, 1], 6) (2, 1)
Element 1, which is 2, needs to be swapped in [7, 2, 3, 4, 5, 6, 1]
[7, 6, 3, 4, 5, 2, 1]
[7, 5, 3, 4, 2, 6, 1]
[7, 4, 3, 2, 5, 6, 1]
[7, 3, 2, 4, 5, 6, 1]
[7, 2, 3, 4, 5, 6, 1]
In the sequence [1, 2, 3, 7, 5, 6, 4] the elements which can't be swapped are:
2 under index 1
3 under index 2
4 under index 6
1 under index 0
In the sequence [1, 2, 3, 6, 5, 4, 7] the elements which can't be swapped are:
2 under index 1
3 under index 2
4 under index 5
1 under index 0
In the sequence [1, 2, 3, 5, 4, 6, 7] the elements which can't be swapped are:
2 under index 1
3 under index 2
4 under index 4
1 under index 0
In the sequence [1, 2, 3, 4, 5, 6, 7] the elements which can't be swapped are:
2 under index 1
3 under index 2
4 under index 3
1 under index 0
In the sequence [1, 2, 4, 3, 5, 6, 7] the elements which can't be swapped are:
2 under index 1
4 under index 2
3 under index 3
1 under index 0
In the sequence [1, 4, 3, 2, 5, 6, 7] the elements which can't be swapped are:
4 under index 1
3 under index 2
2 under index 3
1 under index 0
In the sequence [1, 2, 7, 4, 5, 6, 3] the elements which can't be swapped are:
2 under index 1
4 under index 3
3 under index 6
1 under index 0
In the sequence [1, 2, 6, 4, 5, 3, 7] the elements which can't be swapped are:
2 under index 1
4 under index 3
3 under index 5
1 under index 0
In the sequence [1, 2, 5, 4, 3, 6, 7] the elements which can't be swapped are:
2 under index 1
4 under index 3
3 under index 4
1 under index 0
In the sequence [1, 2, 4, 3, 5, 6, 7] the elements which can't be swapped are:
2 under index 1
4 under index 2
3 under index 3
1 under index 0
In the sequence [1, 2, 3, 4, 5, 6, 7] the elements which can't be swapped are:
2 under index 1
3 under index 2
4 under index 3
1 under index 0
In the sequence [1, 3, 2, 4, 5, 6, 7] the elements which can't be swapped are:
3 under index 1
2 under index 2
4 under index 3
1 under index 0
In the sequence [1, 7, 3, 4, 5, 6, 2] the elements which can't be swapped are:
3 under index 2
4 under index 3
2 under index 6
1 under index 0
In the sequence [1, 6, 3, 4, 5, 2, 7] the elements which can't be swapped are:
3 under index 2
4 under index 3
2 under index 5
1 under index 0
In the sequence [1, 5, 3, 4, 2, 6, 7] the elements which can't be swapped are:
3 under index 2
4 under index 3
2 under index 4
1 under index 0
In the sequence [1, 4, 3, 2, 5, 6, 7] the elements which can't be swapped are:
4 under index 1
3 under index 2
2 under index 3
1 under index 0
In the sequence [1, 3, 2, 4, 5, 6, 7] the elements which can't be swapped are:
3 under index 1
2 under index 2
4 under index 3
1 under index 0
In the sequence [1, 2, 3, 4, 5, 6, 7] the elements which can't be swapped are:
2 under index 1
3 under index 2
4 under index 3
1 under index 0
In the sequence [2, 1, 3, 7, 5, 6, 4] the elements which can't be swapped are:
2 under index 0
3 under index 2
4 under index 6
1 under index 1
In the sequence [2, 1, 3, 6, 5, 4, 7] the elements which can't be swapped are:
2 under index 0
3 under index 2
4 under index 5
1 under index 1
In the sequence [2, 1, 3, 5, 4, 6, 7] the elements which can't be swapped are:
2 under index 0
3 under index 2
4 under index 4
1 under index 1
In the sequence [2, 1, 3, 4, 5, 6, 7] the elements which can't be swapped are:
2 under index 0
3 under index 2
4 under index 3
1 under index 1
In the sequence [2, 1, 4, 3, 5, 6, 7] the elements which can't be swapped are:
2 under index 0
4 under index 2
3 under index 3
1 under index 1
In the sequence [2, 1, 7, 4, 5, 6, 3] the elements which can't be swapped are:
2 under index 0
4 under index 3
3 under index 6
1 under index 1
In the sequence [2, 1, 6, 4, 5, 3, 7] the elements which can't be swapped are:
2 under index 0
4 under index 3
3 under index 5
1 under index 1
In the sequence [2, 1, 5, 4, 3, 6, 7] the elements which can't be swapped are:
2 under index 0
4 under index 3
3 under index 4
1 under index 1
In the sequence [2, 1, 4, 3, 5, 6, 7] the elements which can't be swapped are:
2 under index 0
4 under index 2
3 under index 3
1 under index 1
In the sequence [2, 1, 3, 4, 5, 6, 7] the elements which can't be swapped are:
2 under index 0
3 under index 2
4 under index 3
1 under index 1
In the sequence [3, 2, 1, 7, 5, 6, 4] the elements which can't be swapped are:
3 under index 0
2 under index 1
4 under index 6
1 under index 2
In the sequence [3, 2, 1, 6, 5, 4, 7] the elements which can't be swapped are:
3 under index 0
2 under index 1
4 under index 5
1 under index 2
In the sequence [3, 2, 1, 5, 4, 6, 7] the elements which can't be swapped are:
3 under index 0
2 under index 1
4 under index 4
1 under index 2
In the sequence [3, 2, 1, 4, 5, 6, 7] the elements which can't be swapped are:
3 under index 0
2 under index 1
4 under index 3
1 under index 2
In the sequence [3, 4, 1, 2, 5, 6, 7] the elements which can't be swapped are:
3 under index 0
4 under index 1
2 under index 3
1 under index 2
In the sequence [3, 7, 1, 4, 5, 6, 2] the elements which can't be swapped are:
3 under index 0
4 under index 3
2 under index 6
1 under index 2
In the sequence [3, 6, 1, 4, 5, 2, 7] the elements which can't be swapped are:
3 under index 0
4 under index 3
2 under index 5
1 under index 2
In the sequence [3, 5, 1, 4, 2, 6, 7] the elements which can't be swapped are:
3 under index 0
4 under index 3
2 under index 4
1 under index 2
In the sequence [3, 4, 1, 2, 5, 6, 7] the elements which can't be swapped are:
3 under index 0
4 under index 1
2 under index 3
1 under index 2
In the sequence [3, 2, 1, 4, 5, 6, 7] the elements which can't be swapped are:
3 under index 0
2 under index 1
4 under index 3
1 under index 2
In the sequence [4, 2, 7, 1, 5, 6, 3] the elements which can't be swapped are:
4 under index 0
2 under index 1
3 under index 6
1 under index 3
In the sequence [4, 2, 6, 1, 5, 3, 7] the elements which can't be swapped are:
4 under index 0
2 under index 1
3 under index 5
1 under index 3
In the sequence [4, 2, 5, 1, 3, 6, 7] the elements which can't be swapped are:
4 under index 0
2 under index 1
3 under index 4
1 under index 3
In the sequence [4, 2, 3, 1, 5, 6, 7] the elements which can't be swapped are:
4 under index 0
2 under index 1
3 under index 2
1 under index 3
In the sequence [4, 3, 2, 1, 5, 6, 7] the elements which can't be swapped are:
4 under index 0
3 under index 1
2 under index 2
1 under index 3
In the sequence [4, 7, 3, 1, 5, 6, 2] the elements which can't be swapped are:
4 under index 0
3 under index 2
2 under index 6
1 under index 3
In the sequence [4, 6, 3, 1, 5, 2, 7] the elements which can't be swapped are:
4 under index 0
3 under index 2
2 under index 5
1 under index 3
In the sequence [4, 5, 3, 1, 2, 6, 7] the elements which can't be swapped are:
4 under index 0
3 under index 2
2 under index 4
1 under index 3
In the sequence [4, 3, 2, 1, 5, 6, 7] the elements which can't be swapped are:
4 under index 0
3 under index 1
2 under index 2
1 under index 3
In the sequence [4, 2, 3, 1, 5, 6, 7] the elements which can't be swapped are:
4 under index 0
2 under index 1
3 under index 2
1 under index 3
In the sequence [5, 2, 3, 7, 1, 6, 4] the elements which can't be swapped are:
2 under index 1
3 under index 2
4 under index 6
1 under index 4
In the sequence [5, 2, 3, 6, 1, 4, 7] the elements which can't be swapped are:
2 under index 1
3 under index 2
4 under index 5
1 under index 4
In the sequence [5, 2, 3, 4, 1, 6, 7] the elements which can't be swapped are:
2 under index 1
3 under index 2
4 under index 3
1 under index 4
In the sequence [5, 2, 4, 3, 1, 6, 7] the elements which can't be swapped are:
2 under index 1
4 under index 2
3 under index 3
1 under index 4
In the sequence [5, 4, 3, 2, 1, 6, 7] the elements which can't be swapped are:
4 under index 1
3 under index 2
2 under index 3
1 under index 4
In the sequence [5, 2, 7, 4, 1, 6, 3] the elements which can't be swapped are:
2 under index 1
4 under index 3
3 under index 6
1 under index 4
In the sequence [5, 2, 6, 4, 1, 3, 7] the elements which can't be swapped are:
2 under index 1
4 under index 3
3 under index 5
1 under index 4
In the sequence [5, 2, 4, 3, 1, 6, 7] the elements which can't be swapped are:
2 under index 1
4 under index 2
3 under index 3
1 under index 4
In the sequence [5, 2, 3, 4, 1, 6, 7] the elements which can't be swapped are:
2 under index 1
3 under index 2
4 under index 3
1 under index 4
In the sequence [5, 3, 2, 4, 1, 6, 7] the elements which can't be swapped are:
3 under index 1
2 under index 2
4 under index 3
1 under index 4
In the sequence [5, 7, 3, 4, 1, 6, 2] the elements which can't be swapped are:
3 under index 2
4 under index 3
2 under index 6
1 under index 4
In the sequence [5, 6, 3, 4, 1, 2, 7] the elements which can't be swapped are:
3 under index 2
4 under index 3
2 under index 5
1 under index 4
In the sequence [5, 4, 3, 2, 1, 6, 7] the elements which can't be swapped are:
4 under index 1
3 under index 2
2 under index 3
1 under index 4
In the sequence [5, 3, 2, 4, 1, 6, 7] the elements which can't be swapped are:
3 under index 1
2 under index 2
4 under index 3
1 under index 4
In the sequence [5, 2, 3, 4, 1, 6, 7] the elements which can't be swapped are:
2 under index 1
3 under index 2
4 under index 3
1 under index 4
In the sequence [6, 2, 3, 7, 5, 1, 4] the elements which can't be swapped are:
2 under index 1
3 under index 2
4 under index 6
1 under index 5
In the sequence [6, 2, 3, 5, 4, 1, 7] the elements which can't be swapped are:
2 under index 1
3 under index 2
4 under index 4
1 under index 5
In the sequence [6, 2, 3, 4, 5, 1, 7] the elements which can't be swapped are:
2 under index 1
3 under index 2
4 under index 3
1 under index 5
In the sequence [6, 2, 4, 3, 5, 1, 7] the elements which can't be swapped are:
2 under index 1
4 under index 2
3 under index 3
1 under index 5
In the sequence [6, 4, 3, 2, 5, 1, 7] the elements which can't be swapped are:
4 under index 1
3 under index 2
2 under index 3
1 under index 5
In the sequence [6, 2, 7, 4, 5, 1, 3] the elements which can't be swapped are:
2 under index 1
4 under index 3
3 under index 6
1 under index 5
In the sequence [6, 2, 5, 4, 3, 1, 7] the elements which can't be swapped are:
2 under index 1
4 under index 3
3 under index 4
1 under index 5
In the sequence [6, 2, 4, 3, 5, 1, 7] the elements which can't be swapped are:
2 under index 1
4 under index 2
3 under index 3
1 under index 5
In the sequence [6, 2, 3, 4, 5, 1, 7] the elements which can't be swapped are:
2 under index 1
3 under index 2
4 under index 3
1 under index 5
In the sequence [6, 3, 2, 4, 5, 1, 7] the elements which can't be swapped are:
3 under index 1
2 under index 2
4 under index 3
1 under index 5
In the sequence [6, 7, 3, 4, 5, 1, 2] the elements which can't be swapped are:
3 under index 2
4 under index 3
2 under index 6
1 under index 5
In the sequence [6, 5, 3, 4, 2, 1, 7] the elements which can't be swapped are:
3 under index 2
4 under index 3
2 under index 4
1 under index 5
In the sequence [6, 4, 3, 2, 5, 1, 7] the elements which can't be swapped are:
4 under index 1
3 under index 2
2 under index 3
1 under index 5
In the sequence [6, 3, 2, 4, 5, 1, 7] the elements which can't be swapped are:
3 under index 1
2 under index 2
4 under index 3
1 under index 5
In the sequence [6, 2, 3, 4, 5, 1, 7] the elements which can't be swapped are:
2 under index 1
3 under index 2
4 under index 3
1 under index 5
In the sequence [7, 2, 3, 6, 5, 4, 1] the elements which can't be swapped are:
2 under index 1
3 under index 2
4 under index 5
1 under index 6
In the sequence [7, 2, 3, 5, 4, 6, 1] the elements which can't be swapped are:
2 under index 1
3 under index 2
4 under index 4
1 under index 6
In the sequence [7, 2, 3, 4, 5, 6, 1] the elements which can't be swapped are:
2 under index 1
3 under index 2
4 under index 3
1 under index 6
In the sequence [7, 2, 4, 3, 5, 6, 1] the elements which can't be swapped are:
2 under index 1
4 under index 2
3 under index 3
1 under index 6
In the sequence [7, 4, 3, 2, 5, 6, 1] the elements which can't be swapped are:
4 under index 1
3 under index 2
2 under index 3
1 under index 6
In the sequence [7, 2, 6, 4, 5, 3, 1] the elements which can't be swapped are:
2 under index 1
4 under index 3
3 under index 5
1 under index 6
In the sequence [7, 2, 5, 4, 3, 6, 1] the elements which can't be swapped are:
2 under index 1
4 under index 3
3 under index 4
1 under index 6
In the sequence [7, 2, 4, 3, 5, 6, 1] the elements which can't be swapped are:
2 under index 1
4 under index 2
3 under index 3
1 under index 6
In the sequence [7, 2, 3, 4, 5, 6, 1] the elements which can't be swapped are:
2 under index 1
3 under index 2
4 under index 3
1 under index 6
In the sequence [7, 3, 2, 4, 5, 6, 1] the elements which can't be swapped are:
3 under index 1
2 under index 2
4 under index 3
1 under index 6
In the sequence [7, 6, 3, 4, 5, 2, 1] the elements which can't be swapped are:
3 under index 2
4 under index 3
2 under index 5
1 under index 6
In the sequence [7, 5, 3, 4, 2, 6, 1] the elements which can't be swapped are:
3 under index 2
4 under index 3
2 under index 4
1 under index 6
In the sequence [7, 4, 3, 2, 5, 6, 1] the elements which can't be swapped are:
4 under index 1
3 under index 2
2 under index 3
1 under index 6
In the sequence [7, 3, 2, 4, 5, 6, 1] the elements which can't be swapped are:
3 under index 1
2 under index 2
4 under index 3
1 under index 6
In the sequence [7, 2, 3, 4, 5, 6, 1] the elements which can't be swapped are:
2 under index 1
3 under index 2
4 under index 3
1 under index 6
Then the factorial of three is completed

[Program finished]

"""