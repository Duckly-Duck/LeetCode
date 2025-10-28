class Solution:
    def countValidSelections(self, nums: List[int]) -> int:
        def simulate(arr, start, direction):
            nums = arr[:]  # make a copy
            n = len(nums)
            curr = start
            dir = direction  # +1 for right, -1 for left

            while 0 <= curr < n:
                if nums[curr] == 0:
                    curr += dir
                else:
                    nums[curr] -= 1
                    dir = -dir
                    curr += dir

            return all(x == 0 for x in nums)

        n = len(nums)
        valid = 0

        for i in range(n):
            if nums[i] == 0:
                if simulate(nums, i, 1):   # right
                    valid += 1
                if simulate(nums, i, -1):  # left
                    valid += 1

        return valid
        