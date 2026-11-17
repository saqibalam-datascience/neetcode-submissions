from collections import defaultdict

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        alpha = defaultdict(int)
        left = 0
        length = 0
        ans = 0
        for right in range(len(s)):
            alpha[s[right]] += 1
            while alpha[s[right]] > 1:
                alpha[s[left]]-=1
                left+=1
                

            ans = max(right-left+1, ans)
        
        return ans

                


                