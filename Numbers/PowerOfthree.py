class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n <=0 or type(n)!=int:
            return False
        x = log10(n)/log10(3)
        
        # return n > 0 and log10(n) / log10(3) % 1 == 0
       
        if (x % 1 == 0):
            return True
        else:
            return False
    
        # while n%3==0:
        #     n=n/3
        # return n==1
