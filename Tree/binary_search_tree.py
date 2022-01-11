class Node:
    def __init__(self, key, value, left = None, right = None):
        self.key = key
        self.value = value
        self.left = left
        self.right = right
        

class BST:
    def __init__(self):
        self.root = None
        
        
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
            return Node(k, v)
        if n.key > k:
            n.left = self.insert_item(n.left, k, v)
        elif n.key < k:
            n.right = self.insert_item(n.right, k, v)
        else:
            n.value = v
        return n
    
    
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
    bst = BST()
    bst.insert(500, "apple")
    bst.insert(600, "banana")
    bst.insert(200, "melon")
    bst.insert(100, "orange")
    bst.insert(400, "lime")
    bst.insert(250, "kiwi")
    bst.insert(150, "grape")
    bst.insert(800, "peach")
    bst.insert(700, "cherry")
    bst.insert(50, "pear")
    bst.insert(350, "lemon")
    bst.insert(10, "plum")
    print("preorder traversal : ", end="")
    bst.preorder(bst.root)
    print("\ninorder traversal : ", end="")
    bst.inorder(bst.root)
    print("\n250 : " + bst.search(250))
    bst.delete(200)
    print("200 삭제 후 : ")
    print("preorder traversal : ", end="")
    bst.preorder(bst.root)
    print("\ninorder traversal : ", end="")
    bst.inorder(bst.root)
    
    
