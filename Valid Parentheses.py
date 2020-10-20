class Solution(object):
    def isValid(self, s):
        pairs = {'(': ')', '{': '}', '[': ']'}
        stack = [x for x in s]
        # stack_copy = stack[:]
        # for i in range(1, len(stack), 2):
        #     if stack[i] == pairs[stack[i - 1]]:
        #         stack_copy = stack_copy[:i - 1] + stack_copy[i + 1:]
        # return stack_copy


res = Solution()
print(res.isValid("{[]}"))
