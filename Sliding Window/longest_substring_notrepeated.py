class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        start = 0
        end = 0
        maxl = 1
        longest = []
        
        if s == "":
            maxl = 0
        else:
            while end < len(s):

                if s[end] not in longest:
                    longest.append(s[end])
                    end = end+1
                    # print(longest)
                else:
                    start=start+1
                    end=start
                    longest = []

                if maxl < len(longest):
                    maxl=len(longest)
                
        return maxl
                
