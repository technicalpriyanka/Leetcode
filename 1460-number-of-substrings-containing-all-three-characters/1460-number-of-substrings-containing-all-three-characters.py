class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        substrs = 0
        last_pos = [-1] * 3 # position of [a, b, c]
        for pos in range(len(s)):
            last_pos[ord(s[pos]) - ord("a")] = pos # update index for current char

            # if no valid substsr, 1 + (-1) so 0
            # else, + 1 for current str, + min(last_pos) for chars before current substr as variants
            substrs += 1 + min(last_pos)

        return substrs