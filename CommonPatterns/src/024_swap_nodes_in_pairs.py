class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        
        vals = []
        p = head
        while p:
            val = p.val
            
            if p.next:
                p.val = p.next.val
                p.next.val = val
                p = p.next
                
            p = p.next
            
            
        return head