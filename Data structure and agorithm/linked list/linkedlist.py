#Python linked list

"""
In this project im going to apply one of list-based data structure, linked list.
this script will allow us to: insert, append, prepend and insert in a position
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.next=None

    
class linkedlist:
    def __init__(self):
        self.head =None
    #append an element
    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    #prepend (At the begining of the liked list)
    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    #insert in a specific node
    def insertAfterPosition(self, prev_node, data):
        if not prev_node:
            print("It seems like there is no this position")
            return
        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node
    
    def print_element(self):
        cur_node = self.head
        while cur_node:
            print(cur_node.data)
            cur_node = cur_node.next



llist1 = linkedlist()

llist1.append("EDSON")
llist1.append("JOSE")
llist1.append("CASIMIRO")
llist1.prepend("EU SOU O")
llist1.insertAfterPosition(llist1.head.next, "DA SILVA")
llist1.print_element()






        

