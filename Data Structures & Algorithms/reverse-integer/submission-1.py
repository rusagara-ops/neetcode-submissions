class Solution:
    def reverse(self, x: int) -> int:
        MIN = -2**31
        MAX = 2**31 -1

        sign = 1
        if x < 0:
            sign = -1
            
        x = abs(x)

        result = 0

        while x:
            remainder = x%10
            x = x//10
            result = result*10 + remainder

        result *= sign

        if result > MAX or result < MIN:
            return 0

        return result