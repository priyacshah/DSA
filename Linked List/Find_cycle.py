# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        
        check=[]
        
        while head and head.next!=None:
            if head.next in check:
                return True
            check.append(head.next)
            head=head.next
        return False
#Efficient solution
# fast=slow=head      
#         while fast and fast.next!=None:
#             fast=fast.next.next
#             slow=slow.next
#             if fast==slow:
#                 return True
#         return False
