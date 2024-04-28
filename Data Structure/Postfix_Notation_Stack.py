N = int(input())                               # 피연산자 개수
'''val은 피연산자에 대응하는 값들을 저장할 리스트,
   stk는 계산을 위한 스택, s는 후위 표기식을 입력 받을 문자열'''
val = []                                          
stk = []
s = input()

for _ in range(N):                             # 피연산자 값 입력 받기: N번 반복하여
    val.append(int(input()))                   # val리스트에 피연산자에 대응하는 값을 정수로 입력 받습니다.

for ch in s:                                   # 후위 표기식 계산: 후위 표기식 문자열 s를 한 글짜씩 읽어가면,
    if ch.isalpha():                           # 피연산자면 해당하는 값을 스택에 추가
        stk.append(val[ord(ch) - ord('A')])
    else:                                      # 연산자면 스택에서 필요한 피연산자들을 꺼내 연산한 결과를 다시 스택에 추가
        b = stk.pop()
        a = stk.pop()

        if ch == '+':
            stk.append(a + b)
        elif ch == '-':
            stk.append(a - b)
        elif ch == '*':
            stk.append(a * b)
        else:
            stk.append(a / b)

print(f'{stk[0]:.2f}')                         # 결과 출력: 최종 결과를 스택에서 꺼내어 소숫점 둘째 자리까지 출력합니다.(f-string의 포맷팅 기능 이용)
