class twoSum:
    def twoSum(self, nums, target):
        l = len(nums)
        for i in range(l):
            for j in range(i+1, l):
                if nums[i] + nums[j] == target:
                    return [i, j]


obj = twoSum()
nums = [2, 3, 7]
target = 9
print(obj.twoSum(nums, target))
