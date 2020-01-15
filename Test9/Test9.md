### 9. 回文数（简单）
#### 题目描述
判断一个整数是否是回文数。回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。
##### 示例1:
```
输入: 121
输出: true
```
##### 示例2:
```
输入: -121
输出: false
解释: 从左向右读, 为 -121 。 从右向左读, 为 121- 。因此它不是一个回文数。
```
##### 示例3:
```
输入: 10
输出: false
解释: 从右向左读, 为 01 。因此它不是一个回文数。
```
#### 代码
##### 解法1：转为字符串处理
利用python的切片功能一行代码即可解决。
```python
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        return str(x) == str(x)[::-1]
```
##### 解法2：不利用字符串
翻转整个数值，官方题解有说反转一半，以防溢出，但是溢出不就不是回文数了，因此我觉得不需要考虑溢出。
```python
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        ans = 0
        pri = x
        while x != 0:
            ans = x%10 + ans*10
            x //= 10
        if ans == pri:
            return True
        else:
            return False
```