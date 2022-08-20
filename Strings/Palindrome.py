class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        # n = len(str(x))
        # x = str(x)
        # half = n/2
        # for i in range(half):
        #     print(x[i])
        #     for j in range(n-1,half+1,-1):
        #         first = x[i]
        #         last = x[j]
        #         print(last)
        #         if first == last:
        #             i=i+1
        #         else:
        #             return False
        #         if j == half:
        #             return True
        
        #Efficient solution
        reversed = 0
        while x < reversed:
            reversed = reversed + x%10
            x = x/10
         
        if x == reversed or x == reversed/10:
            return True
#         x= str(x)
#         reverse = x[::-1]
#         if str(x) == reverse:
#             return True
#         else:
#             return False
        
