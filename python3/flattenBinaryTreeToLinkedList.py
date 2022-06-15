# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def move_tree(self, root):
        # 回傳None判斷是否為最後的節點
        if not root:
            return None
        # 取左節點來判斷是否要執行更改二叉樹
        left_tree = self.move_tree(root.left)
        # 在這裡右節點跟左節點得功能不太相同，是抓右邊最尾端
        right_tree = self.move_tree(root.right)
        
        # 如果左邊有子樹就不符合題意所以一旦有左子樹就要修改其結構
        if left_tree:
            # 先把右子樹接到回傳左子樹右端
            left_tree.right = root.right
            # 複製以排序的子樹
            root.right = root.left
            # 清空左子樹
            root.left = None
            
        # 這行return最難。是為了抓右節點所以才寫成這樣
        # 如果右端有直就優先回傳右端為了抓該層最右下的值
        return right_tree or left_tree or root 

    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        
        self.move_tree(root)
