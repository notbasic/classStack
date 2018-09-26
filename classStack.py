class stack():
    def __init__(self):
        self.data = []

    def size(self):
        return len(self.data)

    def isEmpty(self):
        return self.data == 0

    def push(self, item):
        self.data.append(item)
        # self.data.insert(0,item)

    def pop(self):
        return self.data.pop(0)

    def peak(self):
        try:
            return self.data[-1]
        except:
            return self.data == 0


    def __str__(self):
        str_repr = ""
        for el in self.data:
            str_repr += str(el) + "\n"
        str_repr = str_repr.rstrip()

        return str_repr

s = stack()
s.push('(')
s.push(')')
s.push('(')
s.push(')')
s.push(')')
s.push('(')
s.push(')')
s.push('(')
s.push(')')

while s.size != 0:
    if s.peak() == chr(40): # chr(40) is the "("
        s.push(')')
        print('this was a push',s.peak())
    elif s.peak() == chr(41):  # chr(41) is the ")"
        s.pop()
        print('this was a pop',s.peak())
