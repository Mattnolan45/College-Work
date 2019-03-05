class File(object):

   FILE_PERMISSIONS = 'rwx'

   def __init__(self, name, owner, size=0, permissions='null'):
      self.name = name
      self.owner = owner
      self.size = size
      if permissions != 'null':
         self.permissions = ''.join(sorted(permissions))
      else:
         self.permissions = permissions

   def __str__(self):
      return 'File: {}\nOwner: {}\nPermissions: {}\nSize: {} bytes'.format(self.name, self.owner, self.permissions, self.size)

class Folder(object):

   def __init__(self):
      self.d = {}

   def add_file(self, f):
      self.d[f.name] = f

   def del_file(self, name):
      del self.d[name]

   def get_size(self):
      return sum([f.size for f in self.d.values()])

   def __str__(self):
      heading = 'Folder contents'
      uline = '=' * len(heading)
      slist = [heading, uline]
      for k in sorted(self.d.keys()):
         slist.append(self.d[k].__str__())
      slist.append('Folder size: {} bytes'.format(self.get_size()))
      return '\n'.join(slist)
