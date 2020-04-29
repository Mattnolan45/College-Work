import func_bsearch

def count(a,q):
    x=func_bsearch.bsearch(a,q)
    y=func_bsearch.bsearch(a,q+1)
    return y-x
     
       
