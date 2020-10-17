class Solution(object):
    def isPalindrome(self, x):
        if x < 0 or not (-2 ** 31 <= x <= 2 ** 31 - 1):
            return False
        else:
            rev_x = 0
            num = x
            if x > 0:
                while x != 0:
                    digit = x % 10
                    x //= 10
                    rev_x = rev_x * 10 + digit
            else:
                x = abs(x)
                while x != 0:
                    digit = x % 10
                    x //= 10
                    rev_x = rev_x * 10 + digit
                rev_x *= -1
            return num == rev_x


res = Solution()
print(res.isPalindrome(121))
