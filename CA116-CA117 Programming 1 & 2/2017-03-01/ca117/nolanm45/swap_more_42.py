def swap_unique_keys_values(d):
        return({v:k for (k,v) in d.items() if list(d.values()).count(v)==1})
  
def main():
 	print(swap_unique_keys_values(d))

if __name__=="__main__":
 	main()
