import heapq

def find_nth_largest(N, table):
    heap = []

    # 첫 번째 행을 heap에 추가
    for num in table[0]:
        heapq.heappush(heap, num)

    # 다음 행부터는 현재 행의 숫자와 heap의 최소값을 비교하여 큰 값을 heap에 추가
    for i in range(1, N):
        for num in table[i]:
            if num > heap[0]:
                heapq.heappop(heap)
                heapq.heappush(heap, num)

    # heap에서 N번째 큰 수 반환
    return heap[0]

# 입력 받기
N = int(input())
table = [list(map(int, input().split())) for _ in range(N)]

# N번째 큰 수 찾기
result = find_nth_largest(N, table)

# 결과 출력
print(result)
