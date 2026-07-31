class Solution:
    def checkValidString(self, s: str) -> bool:
        stack = []
        star = 0

        for char in s:
            if char == "(":
                stack.append(char)
            if char == "*":
                star += 1
            if char == ")":
                if stack:
                    stack.pop()
                elif star != 0:
                    star -= 1
                else:
                    return False

        if stack and star == len(stack):
            return True
        else:
            return False

