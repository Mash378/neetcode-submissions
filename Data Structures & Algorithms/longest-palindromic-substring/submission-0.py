class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s)<=1:
            return s
        
        n = len(s)
        start = 0
        longest_str = 1
        dp = [[False]*n for _ in range(n)]

        #Base Case
        #One length character
        for i in range(n):
            dp[i][i] = True
        
        #Two word character. True if same
        for i in range(n-1):
            if s[i]==s[i+1]:
                dp[i][i+1]= True
                start = i
                longest_str = 2
            
        for length in range(3, n+1):
            for i in range(n-length+1):
                j = i+length-1
                if s[i]==s[j] and dp[i+1][j-1]:
                    dp[i][j]= True
                    if length>longest_str:
                        start = i
                        longest_str = length

        return s[start:start+longest_str]