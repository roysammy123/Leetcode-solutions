/*
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
For example, 2 is written as II in Roman numeral, just two ones added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9. 
X can be placed before L (50) and C (100) to make 40 and 90. 
C can be placed before D (500) and M (1000) to make 400 and 900.
Given a roman numeral, convert it to an integer.

 

Example 1:

Input: s = "III"
Output: 3
Explanation: III = 3.
Example 2:

Input: s = "LVIII"
Output: 58
Explanation: L = 50, V= 5, III = 3.
Example 3:

Input: s = "MCMXCIV"
Output: 1994
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
*/


// SOLUTION:


class Solution {
public:
    int romanToInt(string s) 
    {
        int number = 0;

        int i=0;

        while(s[i] != '\0')
        {
            if (s[i] == 'I')
            {
                if (s[i+1] == 'V')
                {
                    number += 4;
                    i += 2;
                }

                else if (s[i+1] == 'X')
                {
                    number += 9;
                    i += 2;
                }

                else
                {
                    number += 1;
                    i++;
                }
            }

            else if (s[i] == 'X')
            {
                if (s[i+1] == 'L')
                {
                    number += 40;
                    i += 2;
                }

                else if (s[i+1] == 'C')
                {
                    number += 90;
                    i += 2;
                }

                else
                {
                    number += 10;
                    i++;
                }
            }

            else if (s[i] == 'C')
            {
                if (s[i+1] == 'D')
                {
                    number += 400;
                    i += 2;
                }

                else if (s[i+1] == 'M')
                {
                    number += 900;
                    i += 2;
                }

                else
                {
                    number += 100;
                    i++;
                }
            }

            else if (s[i] == 'V')
            {
                number += 5;
                i++;
            }

            else if (s[i] == 'L')
            {
                number += 50;
                i++;
            }

            else if (s[i] == 'D')
            {
                number += 500;
                i++;
            }

            else if (s[i] == 'M')
            {
                number += 1000;
                i++;
            }
        }

        return number;
    }
};
