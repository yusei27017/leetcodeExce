class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # 取得左右下標
        left, right = 0, len(nums)-1
        
        # 當左指針指到右邊的左邊一格就結束while            
        while left+1 < right:
            # 二分法須先取中線，以中線進行二分下去討論所有狀況
            mid_index = (left + right)//2
            # 如果中線是落在大區域
            if nums[mid_index] > nums[right]:
                # 如果目標在大區的左邊。也就是比中線小又比左邊大。
                if nums[left] <= target <= nums[mid_index]:
                    # 就直接把右指針移動到中線
                    right = mid_index
                else:
                    # 反之沒在左邊，就把左邊整個砍掉
                    left = mid_index
            # 如果中線是落在小區域
            else:
                # 如果目標在小區的右邊。也就是比中線大又比右邊小。
                if nums[mid_index] <= target <= nums[right]:
                    left = mid_index
                else:
                    # 反之沒在右邊，就把右邊整個砍掉
                    right = mid_index

        # 到最後就會收束成兩個下標，查找兩次。
        if nums[right] == target:
            return right
        if nums[left] == target:
            return left
        # 若都查找不到一題意返回 -1
        return -1
