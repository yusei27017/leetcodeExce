# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        c = 0
        sumList = ListNode()
        sumCur = sumList
        curList1 = l1
        curList2 = l2
        while curList1 is not None and curList2 is not None:
            sumCur.next = ListNode()
            nodeSum = curList1.val + curList2.val + c
            c = nodeSum // 10
            sumCur.next.val = nodeSum % 10
            curList1 = curList1.next
            curList2 = curList2.next
            sumCur = sumCur.next
            
        while curList1 is not None:
            sumCur.next = ListNode()
            nodeSum = curList1.val + c
            sumCur.next.val = nodeSum % 10
            c = nodeSum // 10
            curList1 = curList1.next
            sumCur = sumCur.next
            
        while curList2 is not None:
            sumCur.next = ListNode()
            nodeSum = curList2.val + c
            sumCur.next.val = nodeSum % 10
            c = nodeSum // 10
            curList2 = curList2.next
            sumCur = sumCur.next
            
        if c > 0 :
            sumCur.next = ListNode(c)
            
        return sumList.next
