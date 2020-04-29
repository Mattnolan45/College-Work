import sys


class ShopItem(object):

	def __init__(self,desc="",price=0,disc=""):
		self.desc=desc
		self.price=price
		if disc=="yes":
			self.disc=0.2
		else:
			self.disc=0

	def __str__(self):
		return "Description: {}\nPrice: {:.2f}\n20% DIcount:{}".format(self.desc,self.getdiscount(),self.disc)

	def getdiscount(self):
		if self.disc==0.2:
			return self.price * 0.8
		else:
			return self.price

	def comparePrice(self,other):
		if self.getdiscount()>other.getdiscount():
			return -1
		elif self.getdiscount()<other.getdiscount():
			return 1
		elif self.getdiscount()==other.getdiscount():
			return 0



def main():
  
    s=["Persil,5.20,yes","Surf washing powder,5.00,no"]
    p1,p2=s[0].split(","),s[1].split(",")
    p1=ShopItem(p1[0],float(p1[1]),p1[2])
    p2=ShopItem(p2[0],float(p2[1]),p2[2])

    if ShopItem.comparePrice(p1,p2) == 1:
    	print(True)
    else:
    	print(False)


if __name__ == '__main__':
	main()