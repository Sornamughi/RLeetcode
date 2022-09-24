class Solution:
    def convert(self, s, numRows):
        res = ""
        if len(s) == 1:
            return s
        for r in range(numRows):
            increment = (numRows - 1) * 2
            for i in range(r, len(s), increment):
                res = res+s[i]
                if (r > 0) and (r < numRows-1) and i + increment - (2*r) < len(s):
                    res = res + s[i + increment - (2*r)]
        return res


input = "PAYPALISHIRING"
output = "PAHNAPLSIIGYIR"
numRows = 3
obj = Solution()
result = obj.convert(input, numRows)
if result == output:
    print("Expected output: ", output)
    print("Output: ", result)
else:
    print("Error")
