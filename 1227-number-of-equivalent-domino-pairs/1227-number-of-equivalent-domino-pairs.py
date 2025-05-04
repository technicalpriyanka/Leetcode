class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        freq_dict = {}
        for domino in dominoes:
            sorted_domino = tuple(sorted(domino))
            if sorted_domino in freq_dict:
                freq_dict[sorted_domino]+=1
            else:
                freq_dict[sorted_domino]=1
        count = 0
        for freq in freq_dict.values():
            count+=int((freq * (freq-1))/2)
        return count