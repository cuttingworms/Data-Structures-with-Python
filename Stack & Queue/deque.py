from collections import deque

dq = deque("data structure")

for elem in dq:
    print(elem.upper(), end="")
    
print()

dq.append("r")
dq.appendleft("k")

print(dq)

dq.pop()
dq.append("s")

print(dq)

dq.popleft()

print(dq)