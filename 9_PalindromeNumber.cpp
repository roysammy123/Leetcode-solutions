// Given an integer x, return true if x is a palindrome, and false otherwise.

// SOLUTION:

class Solution {
public:
    bool isPalindrome(int x) {
        string s1 = to_string(x); // converting number to string

        string s2 = s1; // duplicating string
      
        reverse(s1.begin(), s1.end()); // reversing original string

        if (s1 == s2)
        {
            return true;
        }
        else
        {
            return false;
        }
    }
};
