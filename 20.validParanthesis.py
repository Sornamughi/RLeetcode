s = "(}{)"

stk = []
for i in range(len(s)):
    if ('{' not in s and '}' in s) or ('(' not in s and ')' in s) or ('{' not in s and '}' in s):
        break
    if (s.count('{') != s.count('}')) or (s.count('[') != s.count(']')) or (s.count('(') != s.count(')')):
        break
    if s[i] == '[' or s[i] == '{' or s[i] == '(':
        stk.append(s[i])
    elif s[i] == ']' and stk[-1] == '[':
        stk.pop()
    elif s[i] == ')' and stk[-1] == '(':
        stk.pop()
    elif s[i] == '}' and stk[-1] == '{':
        stk.pop()
print(stk)
