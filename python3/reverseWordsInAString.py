class Solution:
    def reverseWords(self, s: str) -> str:
        ans = []
        for word in s.split(" ")[::-1]:
            if word:
                ans.append(word)
        return " ".join(ans)
