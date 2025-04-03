class stack:
    def __init__(self):
        self.stack=[]
    def is_empty(self):
        return len(self.stack)==0
    def push(self,item):
        self.stack.append(item)
    def pop(self):
        if self.is_empty():
            return "the stack is empty"
        return self.stack.pop()
    def peek(self):
        if self.is_empty():
            return "the stack is empty"
        return self.stack[-1]
    def display(self):
        print("stack:",self.stack if not self.is_empty() else "empty")

a=stack()
a.push(10)
a.push(20)
a.push(30)
a.push(40)
a.push(50)
a.display()
print(a.pop(),"the top most element is removed from a stack")
print(a.peek(),"it is used to show the top most element in the stack")
a.display()
print(a.is_empty())

