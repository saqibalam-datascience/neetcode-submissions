from collections import defaultdict
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left=0
        right=0
        ans = 0
        h = defaultdict(int)
        while right<len(s):
            h[s[right]]+=1
            while h[s[right]]>1:
                h[s[left]]-=1
                left+=1
            right+=1
            ans = max(ans, right-left)
        return ans