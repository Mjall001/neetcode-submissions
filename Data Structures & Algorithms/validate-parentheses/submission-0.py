class Solution:
    def isValid(self, s: str) -> bool:
        #use dict
        #iterate using for
         #check top of stack[-1] and bracks(c) match
         #if they don't return false
        #else add to stack
        #is stack empty output true

        bracks = {")":"(" , "}":"{" , "]":"["}
        stack = []

        for c in s:

            if stack and c in bracks:
                if stack[-1] == bracks[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)

        return not stack

