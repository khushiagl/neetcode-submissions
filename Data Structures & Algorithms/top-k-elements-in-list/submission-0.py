class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        freq = [[] for i in range(len(nums)+1)]

        for n in nums:
            if n in counts:
                counts[n] += 1
            else:
                counts[n] = 1
        
        for n, c in counts.items():
            print(n)
            print(c)
            freq[c].append(n)
        res = []
        for i in range(len(nums), 0, -1):
            res += freq[i]
            if len(res) == k:
                return res

        