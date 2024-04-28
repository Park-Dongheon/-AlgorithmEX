import sys, heapq                                        # 'sys'모듈과 'heapq'모듈을 임포트합니다.

input = sys.stdin.readline                               # 'sys.stdin.readline'을 'input'함수로 재할당하여 표준 입력에서 빠르게 입력을 받을 수 있도록 합니다.
hq = []                                                  # 빈 리스트 'hq'를 생성합니다. 이 리스트는 절댓값 힙으로 사용됩니다.
for i in range(int(input())):                            # 입력에서 연산의 개수를 읽고, 해당 수만큼 반복합니다.
    x = int(input())                                     # 각 연산에 대한 입력 값을 읽습니다.
    if x == 0:                                           # 입력 값이 0인 경우를 처리합니다.
        print(heapq.heappop(hq)[1] if len(hq) else 0)    # 만약 'hq'리스트에 원소가 있으면, 'heapq.heappop(hq)'를 사용하여 최소값을 꺼내고 해당 튜플의 두번째 요소인 원래 값을 출력합니다. 그렇지 않으면, 0을 출력합니다.
    else:                                                # 입력 값이 0이 아닌 경우를 처리합니다.
        heapq.heappush(hq, (abs(x), x))                  # 절댓값과 원래 값을 튜플로 묶어 최소 힙에 추가합니다. 'abs(x)'를 통해 절댓값을 계산하고, 'x'를 원래 값으로 사용하여 튜플로 만듭니다.

"""이 코드는 입력 연산을 처리하고, 0이 일력될 때마다 절댓값 힙에서 최소값을 출력하고 제거하는 방식으로 동작합니다."""
