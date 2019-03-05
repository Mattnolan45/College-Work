def quicksort(l, beg, fin):
	if fin - beg < 1:
		return
	i = j = beg
	while i <= fin:
		if l[i] <= l[fin]:
			l[i], l[j] = l[j], l[i]
			j += 1
		i += 1
	quicksort(l, beg, j - 2)
	quicksort(l, j, fin)