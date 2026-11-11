from collections import defaultdict, Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t)>len(s):
            return ""

        dict_t = Counter(t) #Keep track of character count
        required = len(dict_t)

        window_counts = {} # Keep track of what we have currently

        formed = 0 # Counts letters with the specific count in we have
        left = 0

        ans = (float("inf"), 0, 0)

        for right, char in enumerate(s):
            window_counts[char] = window_counts.get(char, 0)+1

            if window_counts[char]==dict_t[char]: #Correct letter and frequency present in window
                formed+=1
            
            #Shrink window until now desired
            while left<=right and formed==required:
                character = s[left]

                if (right-left+1)<ans[0]: #Save current window if smallest and contains t  
                    ans = (right-left+1, left, right)

                window_counts[character]-=1
                if character in dict_t and window_counts[character] < dict_t[character]:
                    formed-=1
                
                left+=1
        
        return "" if ans[0] == float("inf") else s[ans[1] : ans[2] + 1]