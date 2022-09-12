d = {}
s = "aabbbccccd"
d = {}
for each in s:
    if each not in d:
        d[each] = 1
    else:
        d[each] += 1

result = 0
odd = 0
for each in d:
    if d[each]%2 == 0:
        result = result + d[each]
    else:
        odd = 1
        result = result + (d[each]-1)

print(result+odd)
