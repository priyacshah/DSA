class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        
        i=0
        l= len(nums)
        
        while i < l:
            if nums[i]==val:
                nums.pop(i)
                l=len(nums)
            else:
                i+=1
        
#         while i<l:
#             if nums[i]==val:
#                 nums[i], nums[l-1] = nums[l-1],nums[i]
#                 nums[l-1-i]='_' 
#                 print(nums)
#             else:
#                 i+=1
                
        return i
        
