class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
#         start=0
#         end=1
        
#         while start<len(nums)-1 and end <len(nums):
#             if start==end:
#                 end+=1
#             if nums[start]-nums[end]==0:
#                 start=start+1
#                 end=0
#             else:
#                 end+=1
#             if start==len(nums)-1 or end==len(nums)-1:
#                 return nums[start]
            
#         return nums[start]
        
        i=0
        for num in nums:
            i=i^num
            
        return i
