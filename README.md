class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class SSL:
    def __init__(self):
        self.head=None
    def prepend(self,data):
        new_node=Node(data)
        new_node.next=self.head
        self.head=new_node
    def delete(self):
        self.head=None
    def display(self):
        c=self.head
        if not c:
            print("list is empty")
            return
        while c:
            print(c.data,end="->")
            c=c.next
        print("None")
p=SSL()
p.prepend(10)
p.prepend(20)
p.prepend(30)
print("before prepending")
p.display()
p.delete()
print("after deleation")
p.display()






