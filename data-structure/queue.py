class Queue:
    def __init__(self, head=None):
        self.storage = [head]

    def enqueue(self, new_element):
        self.storage.append(new_element)

    def peek(self):
        return self.storage[0] 

    def dequeue(self):
        return self.storage.pop(0)
    
# Setup
q = Queue(12)
q.enqueue(20)
q.enqueue(131)
# [1, 2, 3] 1- is oldest

print(q.peek())#  12


print(q.dequeue())# 12 is oldest dequeue

q.enqueue(4) #now [20, 131, 4]

print(q.dequeue())# 20 is oldest
print(q.dequeue()) #13 is the oldest
print(q.dequeue())# 4
q.enqueue(5) # now [5]
print(q.peek()) # 5 is head