import heapq

a = [32, 64 , 34, 76, 36, 63, 11, 678, 11, 88, 61, 74, 13, 26]
print(a)

heapq.heapify(a)    # 최소 힙 만들기
print(a)

result = []
while a:
    result.append(heapq.heappop(a))
print(result)


