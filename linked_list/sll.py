from hashlib import new


class Node():
    def __init__ (self, value):
        self.value = value
        self.next = None

#first_node = Node(21)

class SLL():
    def __init__(self, head):
        self.head = head


# add to front
    def add_front(self, value):
        temp= self.head
        self.head = Node(value)
        self.head.next = temp
        return self

# delete front
    def delete_front(self):
        if(self.head != None):
            temp = self.head
            self.head = self.head.next
            temp=None


# display
    def display(self):
        runner = self.head
        count=1
        str=[]
        while(runner):
            str.append(runner.value)
            count += 1
            runner = runner.next
        print(list1)

# contains
    def contains(self, val):
        runner = self.head
        bol = False
        while(runner):
            if runner.value == val:
                bol =True
            runner = runner.next
        print(bol)



# display number of nodes
    def number_of_nodes(self):
        runner = self.head
        count=0
        while(runner):
            count += 1
            runner = runner.next
        print(f'There are {count} nodes in this list')



newsll = SLL(Node(21))
newsll.add_front(2).add_front(8)
newsll.display()
newsll.number_of_nodes()
