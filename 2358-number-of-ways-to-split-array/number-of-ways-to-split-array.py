class Solution:
    def waysToSplitArray(self, nums: list[int]) -> int:
        n=len(nums)
        prefix_sum_array=[0]*n
        prefix_sum_array[0]=nums[0]
        for i in range(1,n):
            prefix_sum_array[i]= prefix_sum_array[i-1]+nums[i]
        ans=0
        ans = sum( 1 for i in range(n-1) if prefix_sum_array[i]>=prefix_sum_array[-1]-prefix_sum_array[i])
        return ans