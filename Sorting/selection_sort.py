def selection_sort(a):
    for i in range(0, len(a)-1):
        minimum = i
        for j in range(i, len(a)):
            if a[minimum] > a[j]:
                minimum = j
        a[i], a[minimum] = a[minimum], a[i]
        
        
a = [32, 64 , 34, 76, 36, 63, 11, 678, 11, 88, 61, 74, 13, 26]
print(a)
selection_sort(a)
print(a)