from collections import defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        h = defaultdict(int)
        l,r = 0,0
        ans = 0
        max_freq = 0

        while r<len(s):
            h[s[r]]+=1
            max_freq = max(max_freq, h[s[r]])

            while (r-l+1) - max_freq > k:
                h[s[l]]-=1
                l+=1
            
            ans=max(ans, r-l+1)
            r+=1
        return ans