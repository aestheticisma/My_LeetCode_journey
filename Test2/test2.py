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