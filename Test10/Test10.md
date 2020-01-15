### 10. 正则表达式匹配（困难）
#### 题目描述
给你一个字符串`s`和一个字符规律`p`，请你来实现一个支持`'.'`和`'*'`的正则表达式匹配。
```
'.' 匹配任意单个字符
'*' 匹配零个或多个前面的那一个元素
```
所谓匹配，是要涵盖整个字符串`s`的，而不是部分字符串。
* `s`可能为空，且只包含从`a-z`的小写字母。
* `p`可能为空，且只包含从`a-z`的小写字母，以及字符`.`和`*`。

##### 示例1:
```
输入:
s = "aa"
p = "a"
输出: false
解释: "a" 无法匹配 "aa" 整个字符串。
```
##### 示例2:
```
输入:
s = "aa"
p = "a*"
输出: true
解释: 因为 '*' 代表可以匹配零个或多个前面的那一个元素, 在这里前面的元素就是 'a'。因此，字符串 "aa" 可被视为 'a' 重复了一次。
```
##### 示例3:
```
输入:
s = "ab"
p = ".*"
输出: true
解释: ".*" 表示可匹配零个或多个（'*'）任意字符（'.'）。
```
##### 示例4:
```
输入:
s = "aab"
p = "c*a*b"
输出: true
解释: 因为 '*' 表示零个或多个，这里 'c' 为 0 个, 'a' 被重复一次。因此可以匹配字符串 "aab"。
```
##### 示例5:
```
输入:
s = "mississippi"
p = "mis*is*p*."
输出: false
```
#### 代码
##### 解法1：暴力递归
```python
class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        if len(p) == 0:
            return not s
        # 出现'.'的情况
        first = bool(s) and p[0] in (s[0], '.')
        # 出现'*'的情况
        if len(p)>1 and p[1]=='*':
            return self.isMatch(s, p[2:]) or (first and self.isMatch(s[1:], p))
        else:
            return first and self.isMatch(s[1:], p[1:])
```
* 当出现`'.'`的时候，因为它匹配任意字符，因此只要额外判断`p[i]`是否等于`'.'`即可；
* 对于出现`'*'`时，因为它匹配0个到任意个星号前面的字符，所以我们需要对它进行不同的处理，虽然他能匹配0～n个字符，但是对于递归而言，只有两种情况：0个和1个。

##### 解法2: 递归优化
```python
class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        # 定义一个字典作为备忘录
        memo = dict()
        def dp(i, j):
        	# 避免重复计算
            if (i,j) in memo: return memo[(i,j)] 
            if j==len(p): return i==len(s)
            first = i<len(s) and p[j] in (s[i], '.')
            if j<len(p)-1 and p[j+1] == '*':
                ans = dp(i,j+2) or first and dp(i+1,j)
            else:
                ans = first and dp(i+1,j+1)
            memo[(i,j)] = ans
            return ans
        return dp(0,0) 
```
使用两个变量`i`,`j`记录当前匹配到的位置，从而避免使用子字符串切片，并且将`i`,`j`存入备忘录，避免重复计算。