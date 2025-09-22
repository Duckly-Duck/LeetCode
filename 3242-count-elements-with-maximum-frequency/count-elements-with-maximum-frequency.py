class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        d={}
        for i in range(len(nums)):
            d[nums[i]]=d.get(nums[i],0)+1

        max_freq=max(d.values())
        s=sum(value for key,value in d.items() if value == max_freq)

        return s



# efficient
        # freq_counts = collections.Counter(nums)
        # if not freq_counts:
        #     return 0
        
        # max_freq = max(freq_counts.values())
        # max_freq_elements_count = 0

        # for freq in freq_counts.values():
        #     if freq == max_freq: 
        #         max_freq_elements_count += 1
        # return max_freq_elements_count * max_freq