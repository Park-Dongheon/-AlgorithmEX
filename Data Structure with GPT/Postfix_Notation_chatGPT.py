def calculate_postfix(expression, operand_values):
    stack = []

    for char in expression:
        if char.isalpha():  # 피연산자인 경우
            operand_index = ord(char) - ord('A')
            stack.append(operand_values[operand_index])
        else:  # 연산자인 경우
            operand2 = stack.pop()
            operand1 = stack.pop()

            if char == '+':
                result = operand1 + operand2
            elif char == '-':
                result = operand1 - operand2
            elif char == '*':
                result = operand1 * operand2
            elif char == '/':
                result = operand1 / operand2

            stack.append(result)

    return stack[0]

# 입력
N = int(input())
expression = input().strip()
operand_values = [int(input()) for _ in range(N)]

# 후위 표기식 계산
result = calculate_postfix(expression, operand_values)

# 결과 출력
print(f"{result:.2f}")
