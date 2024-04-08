# Python code to practice Linked List

class Node:

    def __init__(self,value):
        self.data = value
        self.next = None

class LinkedList:

    def __init__(self):

        #Create Empty linked list
        self.head = None
        # no of node
        self.n = 0

    def __len__(self):
        return self.n


    def insert_head(self,value):

        #Create new node
        self.new_node = Node(value)

        #create connection
        self.new_node.next = self.head

        #reassign
        self.head = self.new_node

        #increament n
        self.n = self.n + 1


    def __str__(self):

        curr = self.head

        result = ''

        while curr != None:
            result = result + str(curr.data) + '-->'
            curr = curr.next

        return result[:-3]


    def append_val(self,value):

        #Create new node
        new_node = Node(value)

        #check empty list
        if self.head == None:
            new_node = self.head
            self.n = self.n + 1

        else:
        #create a val with curr and assign with head
            curr = self.head

            while curr.next != None:
                curr = curr.next

            #Append new node at the end.
            curr.next = new_node
            self.n = self.n + 1

    def insertAfter(self,after,value):

         #Creating new node
            self.new_node = Node(value)

            #create a val with curr and assign with head
            curr = self.head

            while curr != None:
                if curr.data == after:
                    break
                curr = curr.next

                if curr.next != None:
                    self.new_node.next = curr.next
                    curr.next = self.new_node
                else:
                    return "Item not Found"

            #Increment N
            self.n = self.n + 1




L = LinkedList()
L.insert_head(1)
L.insert_head(2)
L.insert_head(3)
L.insert_head(4)
L.append_val(5)
L.append_val(6)
L.insertAfter(7,100)

print(len(L))
print(L)

