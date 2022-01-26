def balanced(str: str = '') -> bool:
    stack: list = []
    open_braces: str = '({['
    close_braces: str = ')}]'
    flag: bool = True

    for i in str:
        if i in open_braces:
            stack.append(i)
        elif i in close_braces:
            if not stack:
                flag = False
                break
            braces_open = stack.pop()
            if braces_open == '(' and i == ')':
                continue
            elif braces_open == '{' and i == '}':
                continue
            elif braces_open == '[' and i == ']':
                continue
            flag = False
            break
    if flag and len(stack) == 0:
        return True
    return False

if __name__ == '__main__':

    print(balanced('([{}])'))
    print(balanced('([}{])'))

