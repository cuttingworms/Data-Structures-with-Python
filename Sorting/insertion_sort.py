def insertion_sort(a):
    for i in range(1, len(a)):
        for j in range(i, 0, -1):
            if a[j-1] > a[j]:
                a[j], a[j-1] = a[j-1], a[j]
                
                
a = [32, 64 , 34, 76, 36, 63, 11, 678, 11, 88, 61, 74, 13, 26]
print(a)
insertion_sort(a)
print(a)