class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        slow = dummy
        fast = dummy

        # Move fast n + 1 steps ahead to maintain the gap
        for _ in range(n + 1):
            fast = fast.next

        # Move both until fast reaches the end
        while fast:
            slow = slow.next
            fast = fast.next

        # Remove the nth node
        slow.next = slow.next.next

        return dummy.next