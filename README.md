# deleting of entire list
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class SLL_D:
    def __init__(self):
        self.head=None
    def append(self,data):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
            return
        temp=self.head
        while temp.next:
            temp=temp.next
            temp.next=new_node
    def print_list(self):
        if not self.head:
            print("the liked list is empty")
            return
        temp=self.head
        while temp:
            print(temp.data,end="-->")
            temp=temp.next
        print("None")
    def del_SLL(self):
        if self.head is None:
            print("the sll does not exit")
        else:
            self.head=None
            print("sll has been deleted")
l=SLL_D()
l.append(10)
l.append(20)
l.append(30)
print("original list")
l.print_list()
l.del_SLL()
print("after deletion")
l.print_list()




