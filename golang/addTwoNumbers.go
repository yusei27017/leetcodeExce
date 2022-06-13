/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func addTwoNumbers(l1 *ListNode, l2 *ListNode) *ListNode {
    // 先new一個新的鍊表obj，這裡我們用&取地址符。
    newChain := &ListNode{}
    // 把欲返回鏈表簡短聲明給要準備迭代的鏈表obj
    curChain := newChain
    // 令一個進位數
    carry := 0
    // 如果l1 and l2 都有東西的話就進行計算作業直到其中一方沒東西為止
    for l1 != nil && l2 != nil{
        // 先new一個鏈表接在目前鏈表後面
        curChain.Next = &ListNode{}
        // 開始計算，進位數給carry，於除數給新鏈表的值。
        sumVal := l1.Val + l2.Val + carry
        curChain.Next.Val = sumVal % 10
        carry = sumVal / 10
        // 將目前迭代鏈表跟l1 and l2 鏈表往下個鏈表推進
        l1 = l1.Next
        l2 = l2.Next
        curChain = curChain.Next
    }
    // 這是l1太長的情況，基本就是重複上面的操作。
    for l1 != nil{
        curChain.Next = &ListNode{}
        sumVal := l1.Val + carry
        curChain.Next.Val = sumVal % 10
        carry = sumVal / 10
        l1 = l1.Next
        curChain = curChain.Next
    }
    // l2太長同理
    for l2 != nil{
        curChain.Next = &ListNode{}
        sumVal := l2.Val + carry
        curChain.Next.Val = sumVal % 10
        carry = sumVal / 10
        l2 = l2.Next
        curChain = curChain.Next
    }
    // 如果carry還有數字的話則要做最後的進位。理論上來說carry應該非0即1
    if carry != 0 {
        curChain.Next = &ListNode{}
        curChain.Next.Val = carry
        curChain = curChain.Next
    }
    // 鏈表的head.Val是沒有用到的所以要把自己做的鏈表去頭才是題目所要的
    return newChain.Next
}
