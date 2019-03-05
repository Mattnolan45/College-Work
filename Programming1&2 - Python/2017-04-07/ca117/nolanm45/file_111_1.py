class File(object):
  
      FILE_PERMISSIONS="rwx"

      def __init__(self,name,owner,size=0,permissions="null"):
          self.name=name
          self.owner=owner
          self.size=size
          if permissions!= "null":
             self.permissions="".join(sorted(permissions))
          else:
             self.permissions=permissions

      def __str__(self):
          return "File: {}\nOwner: {}\nPermissions: {}\nSize: {} bytes".format(self.name,self.owner,self.permissions,self.size)
