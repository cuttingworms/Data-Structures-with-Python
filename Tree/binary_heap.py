class BHeap:
    def __init__(self, a):
        self.a = a
        self.N = len(a) - 1
    
    
    def create_heap(self):
        for i in range(self.N//2, 0, -1):
            self.downheap(i)
            
            
    def insert(self, key_value):
        self.N += 1
        self.a.append(key_value)
        self.upheap(self.N)
        
        
    def delete_min(self):
        if self.N == 0:
            print("Heap is empty.")
            return None
        
        minimum = self.a[1]
        self.a[1], self.a[-1] = self.a[-1], self.a[1]
        del self.a[-1]
        self.N -= 1
        self.downheap(1)
        return minimum
    
    
    def downheap(self, i):
        while 2 * i <= self.N:
            k = 2 * i
            if k < self.N and self.a[k][0] > self.a[k+1][0]:
                k += 1
            if self.a[i][0] < self.a[k][0]:
                break
            self.a[i], self.a[k] = self.a[k], self.a[i]
            i = k
            
    
    def upheap(self, j):
        while j > 1 and self.a[j // 2][0] > self.a[j][0]:
            self.a[j], self.a[j // 2] = self.a[j // 2], self.a[j]
            j = j // 2  
        
    
    def print_heap(self):
        for i in range(1, self.N+1):
            print("[%d" % self.a[i][0], self.a[i][1], end="]")
        print("\nSize of heap : ", self.N)
        
        
if __name__ == "__main__":
    a = [None] * 1
    a.append([90, "watermelon"])
    a.append([80, "pear"])
    a.append([70, "melon"])
    a.append([50, "lime"])
    a.append([60, "mango"])
    a.append([20, "cherry"])
    a.append([30, "grape"])
    a.append([35, "orange"])
    a.append([10, "apricot"])
    a.append([15, "banana"])
    a.append([45, "lemon"])
    a.append([40, "kiwi"])
    
    bh = BHeap(a)
    print("힙 만들기 전 : ")
    bh.print_heap()
    bh.create_heap()
    print("minimum heap : ")
    bh.print_heap()
    print(bh.delete_min())
    print("최솟값 삭제 후 : ")
    bh.print_heap()
    print("5 삽입 후")
    bh.insert([5, "apple"])
    bh.print_heap()