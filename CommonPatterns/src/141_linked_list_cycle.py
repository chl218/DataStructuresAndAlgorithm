# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        
        p = head
        q = head
        
        while q and p :
            q = q.next
            p = p.next
            if p:
                p = p.next
            else:
                return False
            
            if p == q:
                return True
            
        return False