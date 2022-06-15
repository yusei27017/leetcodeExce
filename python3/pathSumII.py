# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
	//先初始化欲返回的list
        self.ans = []
        
    def pathArray(self, root, targetNum, pathNum):
        //判斷是否到底，如果到底就不用執行下面遞歸，而是跳出。
        if not root:
            return
        
        //每次進入遞歸之前將根植記錄下來，並作為參數傳下去。
        pathNum.append(root.val)
        //向左看
        self.pathArray(root.left, targetNum - root.val, pathNum)
        //向右看
        self.pathArray(root.right, targetNum - root.val, pathNum)
        
        //判斷是否為最底層且 被剪下來的總和 是否等於 根值
        if targetNum == root.val and not root.left and not root.right:
        	//我寫這個我自己也是很醉，為啥不能直接append param
        	//他會返回空，求高人解答
            x = [i for i in pathNum]
            self.ans.append(x)
        
        //退出時把加進去過的路徑值吐出來，以免重複。    
        pathNum.pop()
        return
        
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
    	//檢查題目有沒有給，不給就不解。
        if not root:
            return []

        //開始調用傳入二叉樹，總和，空list
        self.pathArray(root, targetSum, [])

        return self.ans
