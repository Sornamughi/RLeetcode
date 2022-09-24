class Solution:
    def longestPalindrome(self, s: str) -> str:
        result = ''
        resLen = 0
        for i in range(len(s)):
            l = i
            r = i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r-l+1) > resLen:
                    result = s[l:r+1]
                    resLen = r - l + 1
                l -= 1
                r += 1
            l = i
            r = i+1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r-l+1) > resLen:
                    result = s[l:r+1]
                    resLen = r - l + 1
                l -= 1
                r += 1
        return result

s = "cbbd"
obj = Solution()
print(obj.longestPalindrome(s))