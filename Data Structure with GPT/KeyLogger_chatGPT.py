test_case = int(input())

for i in range(test_case):
    L = input()
    password = []
    cursor = 0
    
    for char in L:
        if char == '<':
            cursor = max(0, cursor - 1)
        elif char == '>':
            cursor = min(len(password), cursor + 1)
        elif char == '-':
            if cursor > 0:
                password.pop(cursor - 1)
                cursor -= 1
        else:
            password.insert(cursor, char)
            cursor += 1

    result = ''.join(password)

    print(result)

