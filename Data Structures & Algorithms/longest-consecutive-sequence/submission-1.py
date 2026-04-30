class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums)== 0:
            return 0
        
        nums_set = set(nums)

        max_len = 1

        for num in nums_set:
            if (num - 1) not in nums_set:
                length = 1
                while num + length in nums_set:
                    length += 1
                if length > max_len:
                    max_len = length
        return max_len
            
        
        

        





        