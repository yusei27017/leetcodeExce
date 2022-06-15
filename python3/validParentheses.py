class Solution:
    def isValid(self, s: str) -> bool:
        token_stack = []
        for token in s:
            if token == "{" or token == "(" or token == "[":
                token_stack.append(token)
            elif not token_stack:
                return False
            else:
                if token == "}" and token_stack.pop() != "{":
                    return False
                if token == "]" and token_stack.pop() != "[":
                    return False
                if token == ")" and token_stack.pop() != "(":
                    return False

        if token_stack:
            return False
        else:
            return True
