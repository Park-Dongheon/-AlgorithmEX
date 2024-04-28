# 입력: 책의 개수 N을 받음
N = int(input())

# 책의 판매 기록을 저장할 딕셔너리
book_sales = {}

# 가장 많이 팔린 책의 개수를 추적하는 변수
max_sales_count = 0

# 가장 많이 팔린 책의 제목을 저장하는 변수
best_selling_book = ""

# N개의 책 제목 입력을 받아서 처리
for _ in range(N):
    title = input().strip()  # 책 제목 입력 받음
    # 딕셔너리에 책 판매 기록 업데이트
    if title in book_sales:
        book_sales[title] += 1
    else:
        book_sales[title] = 1

    # 현재 책의 판매 개수가 최대 개수보다 크면 업데이트
    if book_sales[title] > max_sales_count:
        max_sales_count = book_sales[title]
        best_selling_book = title
    # 만약 현재 책의 판매 개수가 최대 개수와 같고, 사전 순서상 앞서면 업데이트
    elif book_sales[title] == max_sales_count and title < best_selling_book:
        best_selling_book = title

# 결과 출력 (대문자로 변환하여 출력)
print(best_selling_book.upper())
