# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#.       在此有定義二叉樹的屬性，裡面有左子樹右子樹，還有根值
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False

        # 在這裡就用減法的方式如果到最底成減到最底層
        target =  targetSum - root.val

        # 在這裡下判斷如果 減到最底層的數值剛好是零 且 
	  # 確保已經到達最底層 所以再加個判斷式 左右子樹皆為空
        if target == 0 and not root.left and not root.right:
	     # 條件達成 路徑存在 把True 向上層傳遞
            return True
        
        if self.hasPathSum(root.left, target) or self.hasPathSum(root.right, target):
	     # 接收到來自下層的傳遞 因為是遞歸 所以繼續往上傳
            return True
