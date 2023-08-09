class Solution:
    def isValid(self, s: str) -> bool:
        
        n = len(s)
        stack = []
        for i in range(0, n):
            if s[i]==')' or s[i]=='}' or s[i]==']':
                if len(stack)==0:
                    return False
            if s[i]=='(' or s[i]=='{' or s[i]=='[':
                stack.append(s[i]);
            elif s[i]==')':
                if stack[-1]=='(':
                    stack.pop()
                else:
                    return False
            elif s[i]==']':
                if stack[-1]=='[':
                    stack.pop()
                else:
                    return False
            elif s[i]=='}':
                if stack[-1]=='{':
                    stack.pop()
                else:
                    return False
        n=len(stack)
        if(n==0):
            return True
        else:
            return False
