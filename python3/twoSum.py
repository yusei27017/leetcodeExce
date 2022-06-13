class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        left = 0
        # 設定左邊的指針好回傳index
        for i in nums:
            right = len(nums) - 1
            while left < right:
                # 當左邊的指針移動到超過右邊就全部遍歷完成，退出。
                if target == i + nums[right]:
                    # 答案只有一組就直接return
                    return [left, right]
                #回圈指針要控制
                right -= 1
            left += 1
        # 題目沒說沒找到要怎辦所以這裡直接隨便return給它
        return [-1, -1]
