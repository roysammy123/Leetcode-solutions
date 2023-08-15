class Solution:
    def countEven(self, num: int) -> int:
        count = 0

        if num < 10:
            for i in range(2, num+1, 2):
                count += 1
            return count
        else:
            for i in range(2, num+1):
                s = str(i)
                l = list(s)
                digsum = 0
                for j in l:
                    digsum += int(j)
                if digsum %2 == 0:
                    count += 1
        return count
