class Node:
    def __init__(self,value=0, next=None) -> None:
        self.value = value
        self.next = next

class LinkedList(obj): # type: ignore
    def __init__(self):
        self.head = Node
    def append(self, value):
        new_nodw = Node(value)
        if self.head is Node:
            self.head = new_nodw
        else:
            current = self.head
            while(current.next):
                current = current.next
            current.next = new_nodw

