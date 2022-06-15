func removeNthFromEnd(head *ListNode, n int) *ListNode {
    if head.Next == nil {
        return nil 
    }
	fastPoint := head
	for ; 0 < n && fastPoint.Next != nil; n-- {
		fastPoint = fastPoint.Next
	}
	
	if n != 0 {
		return head.Next
	}
	slowPoint := head

	for fastPoint.Next != nil {
		fastPoint = fastPoint.Next
		slowPoint = slowPoint.Next
	}
	slowPoint.Next = slowPoint.Next.Next

	return head
}
