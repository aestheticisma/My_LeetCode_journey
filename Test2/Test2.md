### 2. 两数相加（中等）
#### 题目描述
给出两个非空的链表用来表示两个非负的整数。其中，它们各自的位数是按照逆序的方式存储的，并且它们的每个节点只能存储一位数字。
如果，我们将这两个数相加起来，则会返回一个新的链表来表示它们的和。
您可以假设除了数字0之外，这两个数都不会以0开头。
##### 示例
```bash
输入：(2 -> 4 -> 3) + (5 -> 6 -> 4)
输出：7 -> 0 -> 8
原因：342 + 465 = 807
```
#### 代码
这道题明显是提醒我去复习链表操作了，而且最重要的是我好像从来没有在python中使用过链表...没办法只能硬着头皮瞎jb敲了，最开始还是失败了，原因有两个：1.因为要返回结果所以要留一个头指针 2.next指针要熟练。
```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        head = ListNode(0) #定义头指针用来返回结果
        l3 = head #l3用来进行链表操作
        count = 0 #判断是否有进位
        while(l1 or l2): 
            x = l1.val if l1 else 0
            y = l2.val if l2 else 0
            l3.next = ListNode((x+y+count)%10) #从个位数开始计算
            l3 = l3.next #指针移动
            count = (x+y+count)//10 #注意python中的整除有两个//
            if(l1!=None):
                l1 = l1.next
            if(l2!=None):
                l2 = l2.next
        if(count == 1): #如果最后还有有进位
            l3.next = ListNode(1)
        return head.next
```
虽然这道题的难度标的是中等，但感觉只要链表操作熟练了，这道题还是蛮简单的。算了算了别忘了复习链表操作...一定不要忘了返回结果需要头指针哦...