class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        l=collections.Counter(nums)
        return [num for num,freq in l.items() if freq==2]