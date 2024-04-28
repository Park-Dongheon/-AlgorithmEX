import heapq

N = int(input())
min_heap = []

for i in range(N):
    x = int(input())

    if x != 0:
        heapq.heappush(min_heap, (abs(x), x))
    else:
        if min_heap:
            i, min_value = heapq.heappop(min_heap)
            print(min_value)
        else:
            print(0)
