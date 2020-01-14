class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        y, ans = abs(x), 0
        boundry = (1<<31) if x<0 else (1<<31) - 1
        print(boundry)
        while y!=0:
            ans = ans*10 + y%10
            if ans > boundry:
                return 0
            y //= 10
        return ans if x>0 else -ans

if __name__ == '__main__':
    a = Solution()
    print(a.reverse(1563847412))