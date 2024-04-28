''' queue.Queue 대신 리스트 활용:
파이썬의 리스트를 큐처럼 활용할 수 있습니다.
append()로 요소를 뒤에 추가하고, pop(0)으로 요소를 앞에서 제거할 수 있습니다.
하지만 리스트의 pop(0)은 리스트의 첫 번째 요소를 제거할 때마다 모든 요소를 한 칸씩 앞으로 이동시켜야 하므로,
큐가 매우 큰 경우에는 성능 저하가 있을 수 있습니다. '''

my_queue = []
my_queue.append(1)
my_queue.append(2)
my_queue.append(3)

while my_queue:
    item = my_queue.pop(0)
    print(item)
