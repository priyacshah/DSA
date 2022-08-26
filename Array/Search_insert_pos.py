class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        end = len(nums)
        start=0
        mid = end/2
        
        while start<=end and mid<len(nums):
            if nums[mid]==target:
                return mid
            elif nums[mid]>target:
                end=mid-1
            elif nums[mid]<target:
                start=mid+1
            mid=(end+start)//2
        
        if start>end:     
            nums.insert(start,target)
            return start
        else:
            nums.insert(end,target)
            return end
