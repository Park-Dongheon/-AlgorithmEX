''' Queue 모듈 사용 (queue.Queue):
파이썬의 queue 모듈을 사용하여 큐를 구현할 수 있습니다.
queue.Queue 클래스를 사용하여 큐를 생성하고,
put() 메서드로 요소를 추가하고, get() 메서드로 요소를 가져올 수 있습니다. '''

from queue import Queue

my_queue = Queue()
my_queue.put(1)
my_queue.put(2)
my_queue.put(3)

while not my_queue.empty():
    item = my_queue.get()
    print(item)
