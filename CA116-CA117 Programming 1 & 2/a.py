class Stack(object):

    def __init__(self):
        self.l=[]

    def push(self,e):
        return self.l.append(e)

    def pop(self):
        return self.l.pop()
    
    def top(self):
        return self.l[-1]

    def is_empty(self):
        return len(self.l)==0          
    def __len__(self):
        return len(self.l)


class Queue(object):

    def __init__(self):
        self.l=[]

    def enqueue(self,e):
        return self.l.append(e)

    def dequeue(self):
        return self.l.pop(0)

    def first(self):
        return self.l[0]

    def is_empty(self):
        return len(self.l)==0          
    
    def __len__(self):
        return len(self.l)


    
