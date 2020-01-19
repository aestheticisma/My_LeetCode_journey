### 11. 盛最多水的容器（中等）
#### 题目描述
给定n个非负整数a1，a2，...，an，每个数代表坐标中的一个点(i, ai)。在坐标内画n条垂直线，垂直线i的两个端点分别为(i, ai)和(i, 0)。找出其中的两条线，使得它们与x轴共同构成的容器可以容纳最多的水。
**说明**：你不能倾斜容器，且n的值至少为2。
![question_11.jpg](leetcode-day7/question_11.jpg)
图中垂直线代表输入数组[1,8,6,2,5,4,8,3,7]。在此情况下，容器能够容纳水（表示为蓝色部分）的最大值为49。
##### 示例：
```
输入: [1,8,6,2,5,4,8,3,7]
输出: 49
```
#### 代码
##### 解法1：暴力穷举法
本懒狗第一个想到的办法就是写两个for循环穷举所有情况...
```python
class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        maxarea = 0
        for i in range(0, len(height)-1):
            for j in range(i+1, len(height)):
                area = (j-i)*min(height[i], height[j])
                if maxarea < area:
                    maxarea = area
        return maxarea
```
##### 解法2：（双指针法）利用题意中的特点
我们知道，盛水的多少取决于容器最短的那根木板，还有两块木板之间的距离。
我们将初始位置放在列表的开始和末尾，为了增大两块木板之间的面积，我们不得不将较短的木板向内侧移动以寻求更长的木板，这样虽然会导致木板之间的距离变短，但还是有可能找到比初始位置面积要大的情况存在。
```python
class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left, right = 0, len(height)-1
        # 记录面积
        maxarea = 0
        while left < right:
        	# 两块木板之间的距离
            b = right - left
            if height[left] < height[right]:
                h = height[left]
                left += 1
            else:
                h = height[right]
                right -= 1
            area = b*h
            if maxarea < area:
                maxarea = area
        return maxarea
```