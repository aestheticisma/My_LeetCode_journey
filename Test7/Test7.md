### 7. 整数反转（简单）
#### 题目描述
给出一个32位的有符号整数，你需要将这个整数中每位上的数字进行反转。
##### 示例1:
```
输入: 123
输出: 321
```
##### 示例2:
```
输入: -123
输出: -321
```
##### 示例3:
```
输入: 120
输出: 21
```
#### 代码
##### 解法1：弹出和推入数字 & 溢出前进行检查
取出一位数字很显然用到`%`，之后需要用`//`将取出的一位数字从原数值中删去。
```python
class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        y, ans = abs(x), 0
        # 边界
        boundry = (1<<31) if x<0 else (1<<31) - 1
        while y!=0:
            ans = ans*10 + y%10
            if ans > boundry:
                return 0
            y //= 10
        return ans if x>0 else -ans
```
另外利用移位可以很容易表示一个很大的边界值。
##### 解法2: 转化为字符串
```python
class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if -10<x<10:
            return x
        str_x = str(x)
        boundry = 1<<31 if x<0 else (1<<31)-1
        if x>0:
            temp = str_x[::-1]
        else:
            temp = str_x[:0:-1]
        ans = int(temp)
        if ans>boundry:
            return 0
        else:
            return ans if x>0 else -ans
```
在这里再次提醒自己熟悉一下python字符串的切片功能。