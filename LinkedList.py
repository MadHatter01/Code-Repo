class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self, head=None):
        self.head = head

    def append(self, newvalue):
        newNode = Node(newvalue)
        if self.head is None:
            self.head = newNode

            return;

        cur = self.head
        while cur.next:
            cur = cur.next
        else:
            cur.next = newNode


    def traverse(self):
        cur = self.head
        while cur.next:
            print(cur.value)
            cur = cur.next

        print(None)


    def findVal(self, data):
        cur = self.head

        while cur:
            if cur.value == data:
                return cur
            cur = cur.next

        return None


ll = LinkedList()
ll.append(2)
ll.append(10)
ll.append(20)

ll.traverse()
    
