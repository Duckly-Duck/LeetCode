class Solution:
    def hasIncreasingSubarrays(self, nums: List[int], k: int) -> bool:
        max_valid = pre = cur = 0
        
        for i, x in enumerate(nums):
            cur += 1
            
            # Sequence breaks when element >= next element or at end
            if i == len(nums) - 1 or x >= nums[i + 1]:
                max_valid = max(max_valid, cur // 2, min(pre, cur))
                pre = cur
                cur = 0
        
        return max_valid >= k

                

