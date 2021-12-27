class Node:
    def __init__(self, item, n):
        self.item = item
        self.next = n
        
def add(item):
    global size
    global front
    global rear
    new_node = Node(item, None)
    
    if size == 0:
        front = new_node
    else:
        rear.next = new_node
    rear = new_node
    size += 1
    
    
def remove():
    global size
    global front
    global rear
    if size != 0:
        fitem = front.item
        front = front.next
        size -= 1
        if size == 0:
            rear = None
    
        return fitem
    
    
def print_queue():
    p = front
    print("front -> ", end="")
    
    while p:
        if p.next:
            print(p.item, " -> ", end="")
        else:
            print(p.item, end="")
        p = p.next
        
    print(" -> rear")
    
    
size = 0
front = None
rear = None       