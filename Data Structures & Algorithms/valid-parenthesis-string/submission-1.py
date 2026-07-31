class Solution:
    def checkValidString(self, s: str) -> bool:
        stack = []
        stars = []

        for i,char in enumerate(s):
            if char == "(":
                stack.append(i)
            if char == "*":
                stars.append(i)

            if char == ")":
                if stack:
                    stack.pop()
                else:
                    stars.pop()

        while stack and stars:
            if stack.pop() > stars.pop():
                return False

        return not stack


        
                

