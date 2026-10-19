class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        smaller = sum(x < target for x in nums)
        count = nums.count(target)
        return list(range(smaller, smaller + count))