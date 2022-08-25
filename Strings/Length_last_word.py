class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        # p=''
        # temp = ''
        # i=0
        
#         while i < len(s):
#             if s[i] == ' ':
#                 temp = ''
#             else:
#                 temp = temp+s[i]
#                 p=temp
#             i+=1
            
#         return len(p)

        words = s.strip().split(' ')
        return len(words[-1])
        
