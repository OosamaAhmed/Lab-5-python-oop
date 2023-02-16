from q1 import Queue

class Queueq2(Queue):
    mydict={}
    def __init__(self, name, size):
        self.name=name
        self.size=size
        super().__init__()
        Queueq2.mydict[name] =size
    def mysize(self):
        return len(self.list)

    def insert(self, list):
        if self.mysize() == self.size:
            raise Exception("QueueOutOfRange")
        super().insert(list)


x = Queueq2(name="queue1", size=4)
y = Queueq2(name="queue2", size=5)

x.insert(3)
x.insert(4)
x.insert(5)
x.insert(6)
# x.insert(7) # OutOfRangeException
print(x.pop())
print(x.list) #[4, 5, 6]
print(x.mydict) #{'queue1': 4, 'queue2': 5}
