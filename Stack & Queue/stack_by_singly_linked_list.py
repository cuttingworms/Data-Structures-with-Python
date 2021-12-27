class Node:
    def __init__(self, item, link):
        self.item = item
        self.next = link


def push(item):
    global top
    global size
    top = Node(item, top)
    size += 1
    

def peek():
    if size != 0:
        return top.item
    

def pop():
    global top
    global size
    
    if size != 0:
        top_item = top.item
        top = top.next
        size -= 1
        return top_item
    

def print_stack():
    print("top ->\t", end="")
    p = top
    
    while p:
        if p.next != None:
            print(p.item, " -> ", end="")
        else:
            print(p.item, end="")
        p = p.next
        
        
top = None
size = 0        