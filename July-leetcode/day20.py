'''
Remove Linked List Elements

Remove all elements from a linked list of integers that have value val.
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        if head is None: return 
        prev, cur = head, head
        while cur is not None:
            if head.val == val:
                head = cur.next
                prev = cur = head
            elif cur.val == val:
                prev.next = cur.next
                cur = cur.next
            else:
                prev = cur
                cur = cur.next
        return head

#Runtime: 128 ms
#Memory Usage: 16.9 MB