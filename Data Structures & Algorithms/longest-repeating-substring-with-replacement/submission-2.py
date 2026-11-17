from collections import defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        arr = defaultdict(int)
        left = 0
        ans = 0
        for right in range(len(s)):
            arr[s[right]] += 1

            while (right-left+1) - max(arr.values()) > k:
                arr[s[left]] -=1
                left+=1
            
            ans = max(right-left+1, ans)
        return ans
