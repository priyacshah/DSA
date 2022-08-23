class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        #Qs: Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.
        
        
        #Note:
        # ->why start < l1 - if whole string is being traversed and ther is no match             then start will point to after last character. ex: hay = "abcd",needle = "f"
        # ->why i==l2 - if there is only match at the end then it will return start             index of last character so found needle should always be the l2 (i==l2) 
        i=0
        start = 0
        end = 0
        l1 = len(haystack)
        l2 = len(needle)
        
        if not needle:
            return 0
        
        if not haystack or l1<l2:
            return -1
        
        while end < l1 and i < l2:
            if haystack[end]==needle[i]:
                i+=1
                end+=1
            else:
                start+=1
                end=start
                i=0
        return start if start<l1 and i==l2 else -1
    
        
