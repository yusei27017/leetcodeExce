func twoSum(nums []int, target int) []int {
	var right int
	for k, v := range nums {
		right = len(nums) - 1
		for k < right {
			if target == v+nums[right] {
				return []int{k, right}
			} else {
				right--
			}
		}
	}
	return []int{-1, -1}
}
