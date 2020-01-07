### 1. 两数之和（简单）
#### 题目描述
给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那两个整数，并返回他们的数组下标。你可以假设每种输入只会对应一个答案。但是，你不能重复利用这个数组中同样的元素。
##### 示例
```bash
给定 nums = [2, 7, 11, 15], target = 9

因为 nums[0] + nums[1] = 2 + 7 = 9
所以返回 [0, 1]
```
#### 代码
刚开始看到这道题的时候觉得很简单，~~虽然题目本来就标的就是简单.....~~
于是一开始就这样胡乱一写...
```python
class Solution:
    def twoSum(self, nums, target):
        for i in range(0, len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i]+nums[j]==target:
                    return [i, j] 
```
这样写虽然可以做到题目要求，但是时间复杂度太高了$O(n^{2})$，因此提交的时候有时候可以通过，有时候就是时间超过限制，看了评论区各位大佬的提示，讲到可以利用哈希表查找以空间换取时间的做法降低时间复杂度。于是改写代码如下：
```python
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
```
在python里，字典就对应着哈希查找表，于是我们相当于多定义了一个字典，最开始字典为空，按`nums`数组中的顺序取数，首先计算这个数字需要与什么数字相加才能等于`target`，然后就去字典里查找有没有这个数字，如果没有，那就将当前读的数字添加到字典中，key为数字的值，value为标号，所以最后总会在字典中查找到答案，这样时间复杂度就降低到了$O(n)$
第一题就到这里吧，其实DS里的哈希表我也忘记了，emmmm正好趁现在去复习下吧!
