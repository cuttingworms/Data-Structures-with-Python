def downheap(i, size):
    while 2*i <= size:
        k = 2*i
        if k < size and a[k] < a[k+1]:
            k += 1
        if a[i] >= a[k]:
            break
        a[i], a[k] = a[k], a[i]
        i = k
        
        
def create_heap(a):
    hsize = len(a) - 1
    for i in reversed(range(1, hsize // 2 + 1)):
        downheap(i, hsize)
        
        
def heap_sort(a):
    n = len(a) - 1
    for i in range(n):
        a[1], a[n] = a[n], a[1]
        downheap(1, n-1)
        n -= 1
        
        
a = ["None", 64 , 34, 76, 36, 63, 11, 678, 11, 88, 61, 74, 13, 26]
print(a)
create_heap(a)
heap_sort(a)
print(a)