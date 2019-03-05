def maximum(l):
	if len(l)==1:
		return l[0]
	else:
		maxv=maximum(l[1:])
		return l[0] if l[0] > maxv else maxv