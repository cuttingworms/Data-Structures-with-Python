class Node:
    def __init__(self, key, value, height, left = None, right = None):
        self.key = key
        self.value = value
        self.height = height
        self.left = left
        self.right = right
        

class AVL:
    def __init__(self):
        self.root = None
        
        
    def height(self, n):
        if n == None:
            return 0
        return n.height 
    
    
    def rotate_right(self, n):
        x = n.left
        n.left = x.right
        x.right = n
        n.height = max(self.height(n.left), self.height(n.right)) + 1   
        x.height = max(self.height(x.left), self.height(x.right)) + 1
        return x
    
    
    def rotate_left(self, n):
        x = n.right
        n.right = x.left
        x.left = n
        n.height = max(self.height(n.left), self.height(n.right)) + 1   
        x.height = max(self.height(x.left), self.height(x.right)) + 1
        return x
    
    
    def balance(self, n):
        if self.bf(n) > 1:
            if self.bf(n.left) < 0:
                n.left = self.rotate_left(n.left)   # LR 회전
            n = self.rotate_right(n)    # LL 회전
        elif self.bf(n) < -1:
            if self.bf(n.right) > 0:
                n.right = self.rotate_right(n.right)    # RL 회전    
            n = self.rotate_left(n)     # RR 회전
        return n
    
    
    def bf(self, n):
        return self.height(n.left) - self.height(n.right)
    
        
    def search(self, k):
        return self.search_item(self.root, k)
        
    
    def search_item(self, n, k):
        if n == None:
            return None
        if n.key > k:
            return self.search_item(n.left, k)
        elif n.key < k:
            return self.search_item(n.right, k)
        else:
            return n.value
        
        
    def insert(self, k, v):
        self.root = self.insert_item(self.root, k, v)
        
        
    def insert_item(self, n, k, v):
        if n == None:
            return Node(k, v, 1)
        if n.key > k:
            n.left = self.insert_item(n.left, k, v)
        elif n.key < k:
            n.right = self.insert_item(n.right, k, v)
        else:
            n.value = v
            return n
        n.height = max(self.height(n.left), self.height(n.right)) + 1
        return self.balance(n)
    
    
    def find_min(self):
        if self.root == None:
            return None
        return self.find_minimum(self.root)
    
    
    def find_minimum(self, n):
        if n.left == None:
            return n
        return self.find_minimum(n.left)
    
    
    def delete_min(self):
        if self.root == None:
            print("트리가 비어 있음")
        self.root = self.delete_minimum(self.root)
        
        
    def delete_minimum(self, n):
        if n.left == None:
            return n.right
        n.left = self.delete_minimum(n.left)
        return n
    
    
    def delete(self, k):
        self.root = self.delete_node(self.root, k)
        
        
    def delete_node(self, n, k):
        if n == None:   # 삭제할 노드의 자식이 0
            return None
        if n.key > k:
            n.left = self.delete_node(n.left, k)
        elif n.key < k:
            n.right = self.delete_node(n.right, k)
        else:
            if n.right == None: # 삭제할 노드의 자식이 1
                return n.left
            if n.left == None:
                return n.right
            target = n  # 삭제할 노드의 자식이 2
            n = self.find_minimum(target.right)
            n.right = self.delete_minimum(target.right)
            n.left = target.left
            return n
        n.height = max(self.height(n.left), self.height(n.right)) + 1
        return self.balance(n)
    
    
    def preorder(self, n):
        if n != None:
            print(str(n.key), " ", end="")
            if n.left:
                self.preorder(n.left)
            if n.right:
                self.preorder(n.right)
                
                
    def inorder(self, n):
        if n != None:
            if n.left:
                self.inorder(n.left)
            print(str(n.key), " ", end="")
            if n.right:
                self.inorder(n.right)
    
    
if __name__ == "__main__":
    avl = AVL()
    avl.insert(75, "apple")
    avl.insert(80, "grape")
    avl.insert(85, "lime")
    avl.insert(20, "mango")
    avl.insert(10, "strawberry")
    avl.insert(50, "banana")
    avl.insert(30, "cherry")
    avl.insert(40, "watermelon")
    avl.insert(70, "melon")
    avl.insert(90, "plum")
    print("preorder traversal : ", end="")
    avl.preorder(avl.root)
    print("\ninorder traversal : ", end="")
    avl.inorder(avl.root)
    print("\n75와 85 삭제")
    avl.delete(75)
    avl.delete(85)
    print("preorder traversal : ", end="")
    avl.preorder(avl.root)
    print("\ninorder traversal : ", end="")
    avl.inorder(avl.root)
    
    