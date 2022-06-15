class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head.next is None:
            return None

        fast_point = head

        while 0 < n and fast_point.next is not None:
            fast_point = fast_point.next
            n -= 1

        if n != 0:
            return head.next
        slow_point = head

        while fast_point.next is not None:
            fast_point = fast_point.next
            slow_point = slow_point.next

        slow_point.next = slow_point.next.next
        return head
