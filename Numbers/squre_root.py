import math
class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
     # Efficient solution   
#     high=x
#     low=0  
#     while True:
#         half = low + int((high-low)/2)
#         print half

#         if half*half>x:
#             high=half-1
#         else:
#             if(half+1)*(half+1)>x:
#                 return half
#             low=half+1           

        i=1
        count=0
        while x>=0 and i<=x:
            x-=i
            i+=2
            count+=1
        return count
       
        
