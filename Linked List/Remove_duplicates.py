# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

#Link list is sorted
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        start=head
        temp=head
        
        while temp and head.next != None:
            if head.val==head.next.val:
                head.next=temp.next
                temp=head.next
            else:
                temp=temp.next
                head=head.next
        return start
