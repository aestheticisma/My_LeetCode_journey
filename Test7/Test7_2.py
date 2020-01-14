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