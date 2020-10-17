class Solution(object):
    def reverse(self, x):
        digits = str(x)
        result = digits.rstrip('0')
        if x == 0:
            return 0
        elif x < 0:
            result = result[1:]
            result = '-' + result[::-1]
        else:
            result = result[::-1]
        if -2 ** 31 <= int(result) <= 2 ** 31 - 1:
            return result
        else:
            return 0
