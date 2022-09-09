strs = ["how", "horrible"]
n = len(strs)
result = ""
if strs == []:
    result = ""
elif len(strs) == 1:
    result = strs[0]
else:
    strs.sort()
    first = strs[0]
    last = strs[n-1]
    min_length = min(len(first), len(last))
    for i in range(min_length):
        if first[i] == last[i]:
            result = result + first[i]
        else:
            break
print(result)
