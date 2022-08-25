class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        
        l = len(digits)
        digits[l-1] = digits[l-1]+1
        
        while digits[l-1]>9:
            digits[l-1] = 0
            if l>1:
                digits[l-2] = digits[l-2]+1
            else:
                digits.insert(0,1)
            l=l-1
        
        return digits
            
        
        
