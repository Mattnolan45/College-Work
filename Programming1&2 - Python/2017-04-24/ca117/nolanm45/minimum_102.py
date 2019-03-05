def minimum(l):
	if len(l)==1:
		return l[0]
	else:
		minv=minimum(l[1:])
		return l[0] if l[0] < minv else minv