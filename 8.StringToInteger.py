class Solution:
    def myAtoi(self, s: str) -> int:
        res = 0
        sign = 1
        checker = set('0123456789')
        i = 0
        while i < len(s) and s[i] == ' ':
            i += 1

        if i < len(s) and s[i] == '-':
            if i + 1 < len(s) and s[i + 1] == '+':
                return 0
            sign = -1
            i += 1
        if i < len(s) and s[i] == '+':
            if i + 1 < len(s) and s[i + 1] == '-':
                return 0
            i += 1

        while i < len(s) and s[i] in checker:
            res = (res * 10) + int(s[i])
            i += 1

        res = res * sign
        if res < -2 ** 31:
            return -2 ** 31
        elif res > 2 ** 31 - 1:
            return 2 ** 31 - 1
        else:
            return res


x = "   -43"
obj = Solution()
print(obj.myAtoi(x))
