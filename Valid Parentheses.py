def is_valid(s):
    left = {'(': ')', '{': '}', '[': ']'}
    right = {')': '(', '}': '{', ']': '['}
    stack = []
    i = 0
    if len(s) % 2 != 0:
        return False
    while i < len(s):
        stack.append(s[i])
        if s[i] in left and i <= len(s) - 2:
            if s[i + 1] == left[s[i]]:
                stack.pop()
                i += 1
        elif s[i] in right and len(stack) >= 2:
            if stack[-2] == right[s[i]]:
                stack.pop()
                stack.pop()
        i += 1
    return not stack


s = "){"
print(is_valid(s))
