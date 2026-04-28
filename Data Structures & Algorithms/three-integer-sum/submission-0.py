class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        for i in range(len(nums)):
            j = i + 1
            k = len(nums) - 1
            while j < k:
                if nums[j] + nums[k] < - nums[i]:
                    j +=1
                elif nums[j] + nums[k] > - nums[i]:
                    k -= 1
                else:
                    temp = [nums[i], nums[j], nums[k]]
                    if temp not in res:
                        res.append(temp)
                    j += 1

        return res    



        