class Solution:
    def numIdenticalPairs(self, nums):
        from collections import Counter
        freq = Counter(nums)
        count = 0
        for val in freq.values():
            count += (val * (val - 1)) // 2  # nC2 formula
        return count