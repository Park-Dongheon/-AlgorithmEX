import sys, heapq

input = sys.stdin.readline
min_heap = []    # 양수 값을 저장하기 위한 최소힙
max_heap = []    # 음수 값을 저장하기 위한 최대힙
for i in range(int(input())):               # 입력된 연산의 개수만큼 반복합니다.
    x = int(input())                        # 각 연산에 대한 입력 값을 읽습니다.
    if x > 0 :                                    # 입력 값이 양수인 경우, 'min_heap'에 해당 값을 추가
        heapq.heappush(min_heap, x)
    elif x < 0:                                   # 입력 값이 음수인 경우, '-x'를 취한 후 'max_heap'에 추가, 'max_heap'에는 양수가 음수로 변환된 값들이 저장
        heapq. heappush(max_heap, -x)
    else:                                         # 입력 값이 0인 경우 처리합니다.
        if len(min_heap):                                              # 'min_heap'에 원소가 있는 경우에만 아래 코드 블록을 실행
            if len(max_heap) == 0 or min_heap[0] < max_heap[0]:            # 'max_heap'이 비어 있거나 'min_heap'의 최소값이 'max_heap'의 최댓값보다 작으면, 'min_heap'의 최소값을 출력
                print(heapq.heappop(min_heap))
            else:                                                          # 그렇지 않으면, 'max_heap'의 최댓갑을 '-'를 사용하여 양수로 변환한 후 출력
                print(-heapq.heappop(max_heap))
        else:                                                          # 'min_heap'에 원소가 없는 경우에 동작
            print(-heapq.heappop(max_heap) if len(max_heap) else 0)    # 'len(max_heap)'를 사용하여 'max_heap'에 원소가 있는 경우, 'max_heap'의 최댓갑을 '-'를 사용하여 양수로 변환한 후 출력, 그렇지 않은 경우 0을 출력
