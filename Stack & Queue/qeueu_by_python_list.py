queue = []


def add(item):
    queue.append(item)
    

def remove(item):
    if len(queue) != 0:
        item = queue.pop(0)
        return item
    

def print_queue():
    print("front -> ", end="")
    
    for i in range(len(queue)):
        print("{!s:<8}".format(queue[i]), end="")
    
    print(" <- rear")
