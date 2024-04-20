def minRemoveToMakeValid(s: str) -> str:
    stack = []
    result = []
    for c in s:
        if c == '(':
            stack.append(len(result))
            result.append(c)
        elif c == ')':
            if stack:
                stack.pop()
                result.append(c)
        else:
            result.append(c)

    for i in stack:
        result[i] = ''

    return ''.join(result)

    # b = True
    # stack = list()
    # stack_c = list()
    #
    # for indx, ch in enumerate(s):
    #     if ch not in ['(', ')']:
    #         continue
    #     if ch == '(':
    #         stack.append(indx)
    #         b = False
    #     elif ch == ')' and b is False and stack:
    #         stack.pop()
    #         if not stack:
    #             b = True
    #
    #     elif ch == ')' and b is True and stack:
    #         stack_c.append(indx)
    #
    #     elif ch == ')' and b is True and not stack:
    #         stack_c.append(indx)
    #     else:
    #         pass
    # stack += stack_c
    # r = ''.join([char for i, char in enumerate(s) if i not in stack])
    # # print(r)
    # return r


if __name__ == '__main__':
    print('1correct') if minRemoveToMakeValid('))((') == '' else print('1incorrect')
    print('2correct') if minRemoveToMakeValid("a)b(c)d") == "ab(c)d" else print('2incorrect')
    print('3correct') if minRemoveToMakeValid('lee(t(c)o)de)') == "lee(t(c)o)de" else print('3incorrect')
    print('4correct') if minRemoveToMakeValid('f())x)(d))hj(()') == 'f()x(d)hj()' else print('4incorrect')
    # print(minRemoveToMakeValid('f())x)(d))(h)j(())'), 'f()x(d)hj()')
