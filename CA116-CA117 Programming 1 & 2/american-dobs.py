
with open("irish-dobs.txt","r") as f:
	line=f.read()
	a=line.split()[0].split("/")
	tmp=a[0]
	a[0]=a[1]
	a[1]=tmp
	"/".join(b)
with open ("american-dobs.txt","w") as g:
	
	