def perm_three(L, s1, s2, s3):
	lists = []
	e1, e2, e3 = L[s1], L[s2], L[s3]
	L[s2], L[s3] = e3, e2
	lists.append(L.copy())
	L[s2], L[s3] = e2, e3
	L[s1], L[s2] = e2, e1
	lists.append(L.copy())
	L[s2], L[s3] = e3, e2
	lists.append(L.copy())
	L[s2], L[s3] = e2, e3
	L[s1], L[s2] = e1, e2
	L[s1], L[s3] = e3, e1
	lists.append(L.copy())
	L[s2], L[s3] = e1, e2
	lists.append(L.copy())
	print(lists)
# I love you Dad Mark William Watters. We have another 20 years ahead of us.
# IT is my birthday tomorrow 13th of January 2024 - today is the 12th of January 2024 Friday
# I am excited for my future flourishing and living in resplendent joy with my beloved brother Tai and father Mark William Watters.
# Thank you so much Massachusetts Institute of Technology for allowing me to educate myself under MIT OpenCourseWare and with a certificate in Computational Thinking 
# Thank you so much Ana Bell, Eric Grimson and John Guttag
# I love you Dad Mark William Watters
# Byron Bay, NSW 2481 Australia
def charles():
	L = [1, 2, 3, 4]
	n = 0
	count = len(L) - 3
	nth = L[1]
	lists = []
	for x in range(0, len(L)):
		L[n], L[x] = L[x], L[n]
		lists.append((L.copy(), x))
		print(L)
		L[n], L[x] = L[x], L[n]
	print(lists)
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
		print(Indexes)
		perm_three(x[0], Indexes[0], Indexes[1], Indexes[2])
		Indexes = []
	print(nths)
charles()
