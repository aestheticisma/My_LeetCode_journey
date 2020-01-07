class Solution:
    def lengthOfLongestSubstring(self, s):
        dict1 = {} #定义一个字典用来查找
        i , ans = 0, 0 #i代表重复的最后的位置，ans为结果
        for j in range(len(s)):
            if s[j] in dict1:
                i = max(dict1[s[j]],i) #取重复的最后面的字符位置
                #i = dict1[s[j]]
            ans = max(ans, j-i+1) #取最大的子序列长度
            dict1[s[j]] = j+1 #将不在字典中的也就是不重复的字母放入字典
        return ans