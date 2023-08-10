class Solution:
    def mySqrt(self, x: int) -> int:
        if x <= 3 and x!=0:
            return 1
        elif x == 0:
            return 0
        else:
            for i in range(x):
                if (x == i*i):
                    return i
                elif (x > i*i) and (x < (i+1)*(i+1)):
                    return i
