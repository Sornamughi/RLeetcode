def sumOfSquare(num):
    temp = num
    result = 0
    while temp > 0:
        result = result + (temp % 10)**2
        temp = temp // 10
    return result


n = 2
visit = set()
while n not in visit:
    visit.add(n)
    n = sumOfSquare(n)
    if n == 1:
        print("True")
        break
if n!= 1:
    print("False")

