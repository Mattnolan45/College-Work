class Student(object):
     
      def __init__(self,surname,forname,sid,modlist=[]):
          self.sid=sid
          self.surname=surname
          self.forname=forname
          self.modlist=modlist
      
      def add_module(self,mod):
          if mod not in self.modlist:
             self.modlist.append(mod)
          else:
             pass  
      
      def del_module(self,mod):
          if mod in self.modlist:
            self.modlist.remove(mod)          
          
          
          
          

      def print_details(self):
          print("ID: {}".format(self.sid))
          print("Surname: {}".format(self.surname))
          print("Forename: {}".format(self.forname))
          print("Modules: {}".format(" ".join(self.modlist)))          
