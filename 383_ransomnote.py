class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        for i in ransomNote:
            if magazine.count(i) == 0:
                return False
            elif ransomNote.count(i) > magazine.count(i):
                return False
        return True
