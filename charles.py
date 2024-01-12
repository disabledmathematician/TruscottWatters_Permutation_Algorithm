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

# I love you Dad Mark William Watters. We have another 20 years ahead of us.
# IT is my birthday tomorrow 13th of January 2024 - today is the 12th of January 2024 Friday
# I am excited for my future flourishing and living in resplendent joy with my beloved brother Tai and father Mark William Watters.
# Thank you so much Massachusetts Institute of Technology for allowing me to educate myself under MIT OpenCourseWare and with a certificate in Computational Thinking 
# Thank you so much Ana Bell, Eric Grimson and John Guttag
# I love you Dad Mark William Watters
# Byron Bay, NSW 2481 Australia
# Most of the inductive case sound. My solution is to swap all n over 3 elements then complete the factorial of three by allowing storage of all n is greater than 3 elements to be swapped to each other place then complete the permutations of three. To be true to infinity it needs to, say, for gamma six, swap the first to all six places, the second element to all five places except where the first is, the third to all four places, and then complete gamma three for all combinatorially plausible, for example in a queue. Inductive definition is that if the factorial of two can be completed, and the factorial of three can, for all swaps, then the factorial swap of infinity can be completed
# Charles Truscott Watters, 12th of January 2024, one day before my 31st birthday in Byron Bay Australia, where I have lived since 1993 with my father Mark and brother Tai.
def charles():
	L = [1, 2, 3, 4]
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
charles()


""" [1, 2, 3, 4]
[[1, 2, 3, 4], [1, 2, 4, 3], [1, 3, 2, 4], [1, 3, 4, 2], [1, 4, 3, 2], [1, 4, 2, 3]]
[2, 1, 3, 4]
[[2, 1, 3, 4], [2, 1, 4, 3], [3, 1, 2, 4], [3, 1, 4, 2], [4, 1, 3, 2], [4, 1, 2, 3]]
[3, 2, 1, 4]
[[3, 2, 1, 4], [3, 4, 1, 2], [2, 3, 1, 4], [2, 4, 1, 3], [4, 2, 1, 3], [4, 3, 1, 2]]
[4, 2, 3, 1]
[[4, 2, 3, 1], [4, 3, 2, 1], [2, 4, 3, 1], [2, 3, 4, 1], [3, 2, 4, 1], [3, 4, 2, 1]]

PyDroid on a Galaxy Note 20 5G
"""