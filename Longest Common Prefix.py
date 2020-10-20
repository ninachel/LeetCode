class Solution(object):
    def longestCommonPrefix(self, strs):
        prefix = ''
        if strs:
            shortest = sorted(strs, key=len)[0]
            for i in range(len(shortest)):
                if all(x.startswith(shortest[:i + 1]) for x in strs):
                    prefix = shortest[:i + 1]
        return prefix
