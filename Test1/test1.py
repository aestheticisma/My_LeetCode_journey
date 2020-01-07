# 两数之和
class Solution:
    def twoSum(self, nums, target):
        dict1 = {}
        if len(nums)<2:
        	return 0
        for i in range(0,len(nums)):
            num = target - nums[i]
            if num not in dict1:
                dict1[nums[i]] = i
            else:
                return[dict1[num],i]
        return 0