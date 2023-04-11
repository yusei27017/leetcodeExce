class Solution:
    def isPalindrome(self, x: int) -> bool:
        int_string = str(x)
        left, right = 0, len(int_string)-1
        # print(str(x))
        while left < right:
            if int_string[left] != int_string[right]:
                return False
            left += 1
            right -= 1
        return True