class Solution(object):
    def rotate(self, nums, k):
        n = len(nums)
        k = k % n
        res = [0] * n
        for i in range(n):
            res[(i + k) % n] = nums[i]
        nums[:] = res  