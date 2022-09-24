class Solution:
    def reverse(self, x):
        res = 0
        temp = 0
        while x > 0:
            temp = (temp*10) + (x % 10)
            x = x//10
        res = temp
        return res


obj = Solution()
x = 121
if x < 0:
    print("False")
elif x == obj.reverse(x):
    print("True")
else:
    print("False")

