books = dict()                   # books 딕셔너리 생성

for i in range(int(input())):    # 입력 정수만큼 받아 반복문 실행
    name = input()               # 반복 횟수만큼 name 문자열 입력
    if name in books:            # name이 books 딕셔너리에 있을 경우, name키에 대한 value +1씩 누적
        books[name] += 1
    else:                        # name이 books 딕셔너리에 없을 경우, name키에 대한 value = 1
        books[name] = 1

max_val = max(books.values())    # value가 가장 큰 값 찾기
arr = []
for k, v in books.items():
    if v == max_val:
        arr.append(k)

arr.sort()                       # arr리스트 오름차순 정렬
print(arr[0])
