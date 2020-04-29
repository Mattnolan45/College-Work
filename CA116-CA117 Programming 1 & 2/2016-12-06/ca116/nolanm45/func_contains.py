import func_bsearch

def contains(a,q):
   p=func_bsearch.bsearch(a,q)
   
   return p<len(a) and a[p] == q
