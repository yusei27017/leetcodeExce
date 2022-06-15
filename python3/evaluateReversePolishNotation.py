class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        if len(tokens) == 1:
            return int(tokens[0])
        
        num_stack = []
        
        for i in tokens:
            if i == "+" or i == "-" or i == "*" or i == "/":
                num = int(num_stack.pop())
                if i == "+":
                    ans = int(num_stack.pop()) + num
                if i == "-":
                    ans = int(num_stack.pop()) - num
                if i == "*":
                    ans = int(num_stack.pop()) * num
                if i == "/":
                    ans = int(num_stack.pop()) / num
                num_stack.append(ans)
            else:
                num_stack.append(i)

        return int(ans)
