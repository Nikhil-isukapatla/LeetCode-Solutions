class Solution:
    def arrayRankTransform(self, arr):
        sorted_unique = sorted(set(arr))

        rank = {}
        for i, num in enumerate(sorted_unique):
            rank[num] = i + 1

        return [rank[num] for num in arr]