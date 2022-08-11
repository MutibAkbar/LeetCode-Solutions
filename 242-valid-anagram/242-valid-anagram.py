class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) == len(t):
            for temp_s in s:
                if s.count(temp_s) == t.count(temp_s):
                    continue
                return False
            return True
        
        return False
        
        