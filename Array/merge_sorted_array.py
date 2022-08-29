class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        # i=0
        # j=0
        # if m==0:
        #     print("here if")
        #     nums1==nums2
        # else:
        #     print("here")
        #     while j<n:
        #         if nums1[i]<=nums2[j] and m!=0:
        #             i+=1
        #         else:
        #             nums1.insert(i,nums2[j])
        #             j+=1
        #         if nums1[i]==0 and i>=m:
        #             nums1[i]=nums2[j]
        #             j+=1
        # i=len(nums1)-1
        # while  i>=m+n:
        #     nums1.pop()
        #     i-=1
        
        i = m-1
        j = n-1
        x = m+n-1
        
        while i>=0 and j>=0:
            if nums1[i]>=nums2[j]:
                nums1[x]=nums1[i]
                x-=1
                i-=1
            else:
                nums1[x]=nums2[j]
                x-=1
                j-=1
        while i>=0:
            nums1[x]=nums1[i]
            x-=1
            i-=1
        while j>=0:
            nums1[x]=nums2[j]
            x-=1
            j-=1
