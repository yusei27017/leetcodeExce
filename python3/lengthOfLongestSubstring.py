class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        q_arr = []
        # q_dic = defaultdict(int)
        start, max_len = 0, float('-inf')
        for index in range(len(s)):
            # if s[index] == s[]
            while s[index] in q_arr:
                q_arr.pop(0)
            q_arr.append(s[index])
            max_len = max(max_len, len(q_arr))
                
        return max_len if max_len != float('-inf') else 0