height=[1,2,3,8,3,2,1,8,7]
max_area = 0
i= 0
j = len(height)-1
while i<j:
    max_area = max(max_area, (min(height[i],height[j])*(j-1)))
    if height[i] < height[j]:
        i += 1
    else:
        j -= 1
print(max_area)