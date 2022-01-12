def shell_sort(a):
    h = 4   
    while h >= 1:
        for i in range(h, len(a)):
            j = i
            while j >= h and a[j] < a[j-h]:     # 각 그룹에 대한 삽입 정렬
                a[j], a[j-h] = a[j-h], a[j]
                j -= h
        h //= 3


a = [32, 64 , 34, 76, 36, 63, 11, 678, 11, 88, 61, 74, 13, 26]
print(a)
shell_sort(a)
print(a)