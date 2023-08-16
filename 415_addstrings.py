import sys
sys.set_int_max_str_digits(0)

class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        l1 = list(num1)
        l2 = list(num2)

        num1 = 0
        for curr_digit in l1:
            num1 = num1*10 + int(curr_digit)
        num2 = 0
        for curr_digit in l2:
            num2 = num2*10 + int(curr_digit)

        num = num1+num2
        return str(num)
