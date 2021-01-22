# node is any individual element in the linked list
class Node(object):
    def __init__(self, value= None):
        self.value = value
        self.next = None #pointer
    
    def get_value(self):
        return self.value
    def get_next(self):
        return self.next
    def set_next(self, new_next):
        self.next = new_next
""" checking Nodes
node1 = Node(10) 
node2 = Node(1) 
node3 = Node(7)

node1.next = node2 # 10->1
node2.next = node3 # 1->7

print(node1.get_value()) #10
print(node1.get_next().value) #1
node1.set_next(2) # setting next to node1 to be 2 10->2
print(node1.get_next()) #fetting new next which is 2
"""

# wrapper of Node class
class LinkedList(object):
    def __init__(self):
        #first element init node
        self.head = Node() 
    def insert_at_beginning(self, value):
        new_node = Node(value)
        new_node.set_next(self.head) #head element now became the next
        self.head = new_node # new element now bacame th head
    def append(self, value):
        new_element = Node(value)
        current = self.head
        if self.head:
            while current.next:
                current = current.next #move to the end of the list till current.next == Null
            current.next = new_element
        else:
            self.head = new_element
    def length(self):
        current = self.head
        total = 0
        while current.next: #counting till current.next !=None
            total+=1
            current = current.get_next()
        return total

    def display(self):
        elems=[]
        current_node=self.head
        if self.head:
            while current_node.next != None:
                current_node=current_node.next
                elems.append(current_node.value)
        print(elems)
        print(self.length())
    def get(self, index):
        if index >= self.length():
            print('error: index is out of range')
            return None
        current_index = 0
        current_node = self.head
        while True:
            current_node=current_node.next
            if current_index == index:
                return current_node.value
            current_index += 1
    def delete(self, index):
        if index >= self.length():
            print('error: index is out of range')
            return None
        current_index = 0
        current_node = self.head
        while True:
            # in addition to keeping track of the current node, the delete method also remembers the last node it visited
            last_node=current_node
            current_node=current_node.next
            if current_index==index:
                last_node.next = current_node.next # skipping element
                return
            current_index +=1

linked_list1 = LinkedList()
linked_list1.display() # []
linked_list1.append(2)
linked_list1.append(27)
linked_list1.append(1)
linked_list1.append(1234)
linked_list1.display() #[2, 27, 1, 1234]
print(linked_list1.get(3)) #get element at position 3 which is 1234
linked_list1.delete(1) # delete position 1 
linked_list1.display() #[2, 1, 1234]

