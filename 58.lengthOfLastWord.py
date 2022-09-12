i = -1
result = 0
s = "day"
s1 = s.rstrip()
if len(s1) == 1:
    result = 1

while result < len(s1) and s1[i] != " ":
    result += 1
    i -= 1
print(result)
