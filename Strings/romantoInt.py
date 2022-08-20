class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        roman = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        add = 0
        
#         for i in range(len(s)):
#             if s[i] in ['I','X','C'] and s[i+1] in (['V','L','D'] or ['X','C','M']):
#                 add = roman[s[i+1]]-roman[s[i]]
#                 return add
#             else:  
#                 for c in s:
#                     add=add+roman[c]
#                 return add
        
#         Efficient solution
        i = 0
        while i < len(s):
            if (i<len(s)-1 and ((s[i]=='I' and s[i+1] in ['V','X']) or 
                (s[i]=='X' and s[i+1] in ['L','C']) or 
                (s[i]=='C' and s[i+1] in ['D','M']))):
                add = add + roman[s[i+1]]-roman[s[i]]
                i+=2
            else:  
                add=add+roman[s[i]]
                i+=1
        return add
        
