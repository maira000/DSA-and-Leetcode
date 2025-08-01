class Solution:
    def rotate(self, nums, k):
        def reverse(arr, start, end):
            while start < end:
                arr[start], arr[end] = arr[end], arr[start]
                start += 1
                end -= 1

        n = len(nums)
        k = k % n  # in case k > n

        # Step 1: Reverse whole array
        reverse(nums, 0, n - 1)

        # Step 2: Reverse first k elements
        reverse(nums, 0, k - 1)

        # Step 3: Reverse the rest
        reverse(nums, k, n - 1)
