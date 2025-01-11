from collections import Counter

class Solution: 
    def canConstruct(self, s: str, k: int) -> bool:
        if len(s) < k:
            return False
            
        count = Counter(s)
        
        even = odd = 0
        for i in count:
            if count[i] % 2 == 0:
                even += 1
            else:
                odd += 1
        
        return False if odd > k else True