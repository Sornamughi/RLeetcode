class Solution:
    def reverse(self, x):
        res = 0
        if x < 0:
            x = abs(x)
            temp = 0
            while x > 0:
                temp = (temp*10) + x % 10
                x = x//10
            res = -1 * temp
        else:
            temp = 0
            while x > 0:
                temp = (temp*10) + (x % 10)
                x = x//10
            res = temp
        if res not in range(-2**31, 2**31 - 1):
            return 0
        else:
            return res


obj = Solution()
x = 123
print("Reversed Integer: ", obj.reverse(x))
