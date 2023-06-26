class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        #only add open parenthesis if open > close
        #AND open < n
        #valid if open == close == n
        stack = []
        res = []

        def dfs(op, close):
            if op == close == n:
                res.append("".join(stack))
                return
            
            if op < n:
                stack.append("(")
                dfs(op + 1, close)
                stack.pop()
            
            if close < op:
                stack.append(")")
                dfs(op, close + 1)
                stack.pop()
        
        dfs(0, 0)
        return res

            