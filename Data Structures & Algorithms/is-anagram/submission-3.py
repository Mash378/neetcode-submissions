from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_dict = Counter(s)
        t_dict = Counter(t)

        print(s_dict)
        print(t_dict)
        for char in t:
            if char not in s_dict:
                return False
            if s_dict[char]!=t_dict[char]:
                return False

        for char in s:
            if char not in t_dict:
                return False
            if s_dict[char]!=t_dict[char]:
                return False
        return True