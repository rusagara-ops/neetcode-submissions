class Solution:
    
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1.0
        if n < 0:
            x = 1/x
            n = -n
        result = 1

        for _ in range(n):
            result *= x

        return result
