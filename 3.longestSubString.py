s = 'aabbccabcd'
left = 0
substr = set()
max_length = 0
for right in range(len(s)):
    while s[right] in substr:
        substr.remove(s[left])
        left += 1
    substr.add(s[right])
    max_length = max(max_length, right-left+1)
print(max_length)

