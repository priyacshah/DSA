class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        
        i=len(a)-1
        j=len(b)-1
        ans=''
        carry=0
    
        while i>=0 or j>=0 or carry>0:
            if i<0:
                tempa=0
            else:
                tempa=int(a[i]) 
            if j<0:
                tempb=0
            else:
                tempb=int(b[j])
                
            temp=tempa+tempb+carry
            
            if temp>=2:
                temp%=2
                carry=1
            else:
                carry=0
            ans = str(temp)+ans
            i-=1
            j-=1
                       
        return ans
