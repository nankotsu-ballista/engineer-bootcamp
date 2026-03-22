N = int(input())
S = input()

stack = []
open_pos = []

for c in S:
    if c == '(':
        open_pos.append(len(stack))
        stack.append(c)
    elif c == ')':
        if open_pos:
            del stack[open_pos.pop():]
        else:
            stack.append(c)
    else:
        stack.append(c)

print(''.join(stack))
