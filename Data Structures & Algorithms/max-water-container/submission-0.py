class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # max amount = smaller height * diff of indices

        # brute force: check every pair and pick the max
        # will take n^2 time

        #better approach : try using 2 pointers

        l = 0
        r = len(heights) - 1
        curr_max = (r-l)*min(heights[l], heights[r])

        while l< r:
            if heights[l] <= heights[r]:
                l = l+1
            else:
                r = r -1
            curr_max = max((r-l)*min(heights[l], heights[r]), curr_max)
        return curr_max    
        

