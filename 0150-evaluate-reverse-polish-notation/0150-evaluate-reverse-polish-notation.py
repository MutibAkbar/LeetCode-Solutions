class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        stack = []
      
        
        for token in tokens:
            if token.isdigit() or (token.startswith('-') and token[1:].isdigit()):
                stack.append(int(token))
            else:
                b = stack[-1]
                a = stack[-2]
           
                del stack[-1]
                del stack[-1]
                
                if token == '+':
                    stack.append(a+b)
                elif token == '-':
                    stack.append(a-b)
                elif token == '*':
                    stack.append(a*b)
                else:
                    stack.append(int(a/b))
                
        return stack[0]
            