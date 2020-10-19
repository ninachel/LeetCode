class Solution(object):
    def romanToInt(self, s):
        result = 0
        result += s.count('I')
        result += s.count('V') * 5
        if 'IV' in s:
            result += 4
            result -= 5
            result -= 1
        result += s.count('X') * 10
        if 'IX' in s:
            result += 9
            result -= 1
            result -= 10
        result += s.count('L') * 50
        if 'XL' in s:
            result += 40
            result -= 10
            result -= 50
        result += s.count('C') * 100
        if 'XC' in s:
            result += 90
            result -= 10
            result -= 100
        result += s.count('D') * 500
        if 'CD' in s:
            result += 400
            result -= 100
            result -= 500
        result += s.count('M') * 1000
        if 'CM' in s:
            result += 900
            result -= 100
            result -= 1000
        return result


# class Solution:
#     def romanToInt(self, s):
#         values = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
#         lst_roman = list(s)
#         lst = lst_roman
#         for i in range(len(lst_roman)):
#             lst[i] = values[lst_roman[i]]
#         for i in range(1, len(lst)):
#             if lst[i] > lst[i - 1]:
#                 lst[i] = lst[i] - lst[i - 1]
#                 lst[i - 1] = 0
#         return sum(lst)

