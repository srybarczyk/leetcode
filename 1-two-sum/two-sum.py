class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i,number1 in enumerate(nums):
            for j,number2 in enumerate(nums):
                if j != i:
                    if number1+number2==target:
                        ans=[i, j]
                        return ans