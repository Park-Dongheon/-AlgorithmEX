import heapq

hq = []                                    # 최소 힙을 저장할 리스트인 hq를 초기화
N = int(input())
for _ in range(N):
    for i in map(int, input().split()):    # 사용자로부터 공백으로 구분된 숫자를 입력받아서 각 숫자에 대해 반복
        if len(hq) >= N:                   # 만약 hq의 길이가 N보다 크거나 같으면,
            heapq.heappushpop(hq, i)       # 최소 힙에 i를 추가한 후 가장 작은 값을 제거
        else:                              # 그렇지 않으면, 최소 힙에 i를 추가
            heapq.heappush(hq, i)
            
print(heapq.heappop(hq))
