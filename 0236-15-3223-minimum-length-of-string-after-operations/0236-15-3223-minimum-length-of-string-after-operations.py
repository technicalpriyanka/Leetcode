class Solution:
    def minimumLength(self, s: str) -> int:
        
        char_counts = Counter(s)
        
        min_length = sum(1 if count % 2 else 2 for count in char_counts.values())
        
        return min_length