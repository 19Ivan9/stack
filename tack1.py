def stack_fun(str: str = '') -> str:
    stack = []
    revers_str = ''
    for i in str:
        stack.append(i)
    for i in str:
        revers_str += stack.pop()
    return revers_str


if __name__ == '__main__':
    my_str = 'ytrewq'
    print(stack_fun(my_str))
