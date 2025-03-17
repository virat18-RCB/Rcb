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
    #deletion on ddl
    class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DDL:  # Doubly Linked List
    def __init__(self):
        self.head = None

    def IAB(self, data):  # Insert At Beginning
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def remove(self, data):
        c = self.head
        while c:
            if c.data == data:
                if c.prev:
                    c.prev.next = c.next
                else:
                    self.head = c.next  # Node to remove is the head
                if c.next:
                    c.next.prev = c.prev
                return  # Exit after removing the node
            c = c.next

    def display(self):
        c = self.head
        if not c:
            print("List is empty")
            return

        while c:
            print(c.data, end="<->")
            c = c.next
        print("None")

# Test the doubly linked list
a = DDL()
a.IAB(10)
a.IAB(20)
a.IAB(30)

print("Before remove in DDL:")
a.display()

a.remove(20)

print("After removing 20:")
a.display()






