import func_bsearch

def sum_range(a,low,high):
    low=func_bsearch.bsearch(a,low)
    high=func_bsearch.bsearch(a,high)
   
    i=high
    j=low
    
    total=0
    while i<j:
      total=total+a[i]
      i=i+1
    return total 
