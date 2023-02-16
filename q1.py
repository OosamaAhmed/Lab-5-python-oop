
class Queue:
    def __init__(self):
        self.list = [] #empty list 

    def insert(self, insert_value):
        self.list.append(insert_value)
    def isEmpty(self):
            return len(self.list) == 0
    
    def pop(self):
         if self.isEmpty():
            print("Empty list (NONE)")
         else:
            return self.list.pop(0)
  
###################
x=Queue()
x.insert(1)
x.insert(2)
x.insert(3)
x.insert(4)
x.insert(5)
x.pop()
print(x.list)

