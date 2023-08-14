class Solution:
    def addDigits(self, num: int) -> int:
        s = str(num)
        x = list(s)
        
        while (len(x)>1):
            add = 0
            for i in x:
                add += int(i)
            s = str(add)
            x = list(s)

        return int(x[0])
