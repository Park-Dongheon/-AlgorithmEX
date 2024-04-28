from collections import deque

N = int(input())
card = range(1, N + 1)
dq = deque()

for i in card:
    dq.append(i)
    
while len(dq) > 1:
    dq.popleft()
    dq.append(dq.popleft())
    
print(dq.pop())
