class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0 
        r = 0
        n = len(s)
        curr_max = r - l + 1
        if n == 0:
            return 0

        seen = set()
        while r < n:
            if s[r] in seen:
                seen.remove(s[l])
                l = l + 1
            else:
                seen.add(s[r])
                r = r+ 1
            curr_max = max(curr_max, r -l )    
        return curr_max