class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counts = {s[0]: 1}
        l = 0
        r = 1
        curr_max = 1
        while r < len(s):
            max_freq = max(counts.values())   
            remaining = sum(counts.values()) - max_freq
            if remaining <= k:
                if s[r] in counts:
                    counts[s[r]] += 1
                else:
                    counts[s[r]] = 1
                max_freq = max(counts.values())   
                remaining = sum(counts.values()) - max_freq
                print(r)
                print(counts)
                print(max_freq)
                print(remaining)
                curr_max = max(max_freq + min(remaining, k), curr_max)
                r += 1
            else:
                counts[s[l]] -= 1
                l = l+1
           
            

        return curr_max