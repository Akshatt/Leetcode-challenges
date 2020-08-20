'''
Reorder List

Given a singly linked list L: L0→L1→…→Ln-1→Ln,
reorder it to: L0→Ln→L1→Ln-1→L2→Ln-2→…

You may not modify the values in the list's nodes, only nodes itself may be changed.

Example 1:
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, H) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if H == None: return None
        C, A = H, []
        while C != None: A.append(C); C = C.next
        M = len(A)//2
        for i in range(M): A[i].next, A[-(i+1)].next = A[-(i+1)], A[i+1]
        A[M].next = None
        return 

#Runtime: 92 ms
#Memory Usage: 23.1 MB