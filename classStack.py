class stack():
    def __init__(self):
        self.data = []

    def size(self):
        return print(len(self.data))

    def isEmpty(self):
        return print(self.data == [])

    def push(self, item):
        self.data.append(item)
        # self.data.insert(0,item)

    def pop(self):
        return print("popped off:",self.data.pop(0))

    def peak(self):
        return print(self.data[-1])

    def str(self):
        strace =""
        for el in (self.data):
            print(str(el+ strace))

s = stack()
s.push(1)
s.push(12)
s.push(123)
s.push(43)
s.push(5)
s.push(764)
s.push(8)
s.str()
s.pop()
s.pop()
s.str()
