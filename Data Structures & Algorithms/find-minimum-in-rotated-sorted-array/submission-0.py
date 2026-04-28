class Solution:
    def findMin(self, nums: List[int]) -> int:
        mid = len(nums) // 2
        l, r = 0, len(nums) - 1
        curr_min = nums[mid]

        while nums[l] > nums[r]:
            if nums[mid] >= nums[l]:
                l = mid + 1
                mid = (l+r)//2
                curr_min = min(curr_min, nums[mid])
            else:
                r = mid - 1
                mid = (l+r)//2
                curr_min = min(curr_min, nums[mid])    
        return min(curr_min, nums[l])


        