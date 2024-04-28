''' collections.deque 사용:
collections 모듈의 deque (Double-Ended Queue)를 사용하여 큐를 구현할 수 있습니다.
deque는 양쪽에서 요소를 추가하고 제거하는 데 효율적이며, 큐로 활용할 수 있습니다.
append()로 요소를 추가하고, popleft()로 요소를 가져옵니다. '''

from collections import deque

my_queue = deque()
my_queue.append(1)
my_queue.append(2)
my_queue.append(3)

while my_queue:
    item = my_queue.popleft()
    print(item)
