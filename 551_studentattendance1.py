class Solution:
    def checkRecord(self, s: str) -> bool:
        if s.count('A') > 1:
            return False
        else:
            for i in range(0, len(s)-2):
                if s[i]=='L' and s[i+1]=='L' and s[i+2] == 'L':
                    return False
        return True
