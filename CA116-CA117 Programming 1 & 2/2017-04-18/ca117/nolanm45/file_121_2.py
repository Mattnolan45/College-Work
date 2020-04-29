class File(object):
   
      FILE_PERMISSIONS="rwx"
 
      def __init__(self,name,owner,size=0,permissions= ""):
          self.name=name
          self.owner=owner
          self.size=size
          self.permissions=permissions
          if self.permissions=="":
            self.permissions="null"
          else:
            self.permissions= "".join(sorted(self.permissions))
 
      def __str__(self):
          return"File: {}\nOwner: {}\nPermissions: {}\nSize: {} bytes".format(self.name,self.owner,self.permissions,self.size)
          
      def has_access(self,n,perm):
          if self.owner==n:
             return True
          elif perm in self.permissions:
             return True
          else:
             return False

                 
