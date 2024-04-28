''' queue.LifoQueue (스택으로 사용):
queue.LifoQueue는 후입선출(LIFO - Last-In-First-Out) 스택을 구현하는 데 사용됩니다.
그러나 이것도 큐처럼 활용할 수 있습니다.
put()로 요소를 추가하고, get()으로 요소를 가져올 수 있습니다. '''

from queue import LifoQueue

my_queue = LifoQueue()
my_queue.put(1)
my_queue.put(2)
my_queue.put(3)

while not my_queue.empty():
    item = my_queue.get()
    print(item)
