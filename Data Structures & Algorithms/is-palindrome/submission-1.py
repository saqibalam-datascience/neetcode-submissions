class Solution:
    def isPalindrome(self, s: str) -> bool:
        sent = ''.join(char.lower() for char in s if char.isalnum())
        i,j = 0, len(sent)-1

        while i<=j:
            if sent[i]!=sent[j]:
                return False
            i+=1
            j-=1

        return True