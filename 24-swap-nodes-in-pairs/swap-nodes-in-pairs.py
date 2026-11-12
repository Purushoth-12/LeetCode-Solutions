class Solution:
    def swapPairs(self, head: ListNode | None) -> ListNode | None:
        dummy = ListNode(0, head)
        prev = dummy
        
        while prev.next and prev.next.next:
            first = prev.next
            second = prev.next.next
            
            # Swapping
            first.next = second.next
            second.next = first
            prev.next = second
            
            # Move prev pointer two nodes forward
            prev = first
            
        return dummy.next