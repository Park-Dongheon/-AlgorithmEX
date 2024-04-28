import sys

input = sys.stdin.readline

n = int(input())

s = set()
for i in range(n):
    name, el = input().split()
    if el == 'enter':
        s.add(name)
    else:
        if name in s:
            s.remove(name)

for name in sorted(s, reverse=True):
    '''s를 역순으로 정렬한 결과인 리스트를 순회합니다.
       집합 안에 남은 사람들의 이름을  내림차순 정렬'''
    print(name)
