class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        non_duplicates = set()
        for i in range(0,len(nums)):
            if nums[i] in non_duplicates:
                return True
            non_duplicates.add(nums[i])
            
        return False