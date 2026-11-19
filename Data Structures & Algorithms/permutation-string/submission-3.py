from collections import defaultdict
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2)<len(s1):
            return False
        h_s1 = defaultdict(int)
        h_s2 = defaultdict(int)
        for i in s1:
            h_s1[i]+=1
        l=0
        r=len(s1)
        
        
        for i in range(r):
            h_s2[s2[i]]+=1

        while r<len(s2):
            if h_s1 == h_s2:
                return True
            h_s2[s2[l]]-=1
            if h_s2[s2[l]] == 0:
                del h_s2[s2[l]]

            l+=1
            h_s2[s2[r]]+=1
            r+=1
        
        if h_s1 == h_s2:
            return True
        return False


