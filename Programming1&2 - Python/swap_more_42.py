
def swap_unique_keys_values(d):
    items=list(d.items())
    for w in items:
    	if items.count(w)>1:
    		d.popitem(d[w])
    		for s in items:
    			if s==w:
    				d.popitem(d[s])

    d={v:k for (k,v) in d.items()}
    return(d)



def main():
	swap_unique_keys_values(items)

if __name__=="__main__":
	main()