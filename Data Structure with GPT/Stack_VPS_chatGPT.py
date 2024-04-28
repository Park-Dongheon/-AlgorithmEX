def is_valid_parentheses(s):
    stack = []  # 스택을 사용하여 괄호 매칭 확인

    for char in s:
        if char in '(':
            stack.append(char)
        else:
            if not stack:
                return False
            if char == ')' and stack[-1] == '(':
                stack.pop()
            else:
                return False

    return not stack  # 스택이 비어 있으면 올바른 괄호 문자열

# 입력 처리
T = int(input())
for _ in range(T):
    parentheses_string = input()
    if is_valid_parentheses(parentheses_string):
        print("YES")
    else:
        print("NO")
