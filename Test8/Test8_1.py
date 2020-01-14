class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        return max(min(int(*re.findall(r'^[\+\-]?\d+', str.lstrip())), (1<<31)-1),\
        -(1<<31))