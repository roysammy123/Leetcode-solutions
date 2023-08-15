class Solution:
    def getLucky(self, s: str, k: int) -> int:
        l = ''
        for i in s:
            l += str(ord(i)-96)
        x = list(l)
        
        while (k > 0):
            add = 0
            for i in x:
                add += int(i)
            news = str(add)
            x = list(news)
            k -= 1

        number = 0
        for current_digit in x:
            number = number*10 + int(current_digit)
        return number
