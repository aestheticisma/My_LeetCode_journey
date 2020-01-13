嘿！大家好，懒狗又要开始更新Leetcode咯！<!--more-->
### 6. Z字形变换（中等）
#### 题目描述
将一个给定字符串根据给定的行数，以从上往下、从左到右进行 Z 字形排列。
比如输入字符串为`"LEETCODEISHIRING"`行数为3时，排列如下：
```
L   C   I   R
E T O E S I I G
E   D   H   N
```
之后，你的输出需要从左往右逐行读取，产生出一个新的字符串，比如：`"LCIRETOESIIGEDHN"`。
请你实现这个将字符串进行指定行数变换的函数：
`string convert(string s, int numRows);`
##### 示例1:
```bash
输入: s = "LEETCODEISHIRING", numRows = 3
输出: "LCIRETOESIIGEDHN"
```
##### 示例2:
```bash
输入: s = "LEETCODEISHIRING", numRows = 4
输出: "LDREOEIIECIHNTSG"
解释:

L     D     R
E   O E   I I
E C   I H   N
T     S     G
```
#### 代码
##### 解法1：按行取值（就叫找规律吧...）
我们可以从这个Z字形（大哥这明明就是N字形啊）的排列上找出些规律，比如如果`numRows = 3`，那么第一行的两个元素相差的距离为4，也就是`d = 2*numRows-2`，最后一行亦如此，而从示例2我们可以看出，中间各行的元素间隔虽然不相等，但是只有两种分布，一种比第一行的`d`要少一部分，而这一部分就是`2*距离第一行的行数差`，那另一种元素间隔就是`d-刚刚那种元素间隔`，就这么简单？还真就这么被找规律找出来了hhh，我都想笑了。
```python
class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1 or numRows >= len(s):
            return s
        else:
            ans = []
            i = 0
            n = 2*numRows-2
            # 第一行
            while i < len(s):
                ans.append(s[i])
                i += n
            # 中间各行
            for i in range(2,numRows):
                n = n - 2
                while i-1 < len(s):
                    ans.append(s[i-1])
                    i += n
            # 最后一行
            n = 2*numRows-2
            i = numRows-1
            while i < len(s):
                ans.append(s[i])
                i += n
            return ''.join(ans)
```
但是看完评论区另一种解法我气的够呛，卧槽我怎么能这么傻，害，这么明显的规律我都没发现...
##### 解法3：按列取值（我觉得更像顺藤摸瓜，嘻嘻嘻）
上一种方法是从`s`中按最终答案的顺序取值，那我们能不能换个思考方式，按照`s`的存储顺序取值呢。
```python
class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows >= len(s) or numRows == 1:
            return s
        ans, count, d = ['']*numRows, 0, 1
        for i in s:
            ans[count] += i
            count += d
            # 当到第一行和最后一行的时候d需要反转
            if count==0 or count==numRows-1:
                d = -d
        return ''.join(ans)
```