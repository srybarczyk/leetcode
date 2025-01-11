class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        prefix_array=[x+extraCandies for x in candies]
        max_candies=max(candies)
        bool_array=[val>=max_candies for val in prefix_array]
        return bool_array