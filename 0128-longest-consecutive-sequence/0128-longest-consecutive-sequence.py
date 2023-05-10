class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        previous_count = 0

        nums = set(nums)
        for num in nums:
            sequence_count = 1
            count = 1
            if num-sequence_count not in nums:
                while(num + sequence_count in nums):
                   count += 1
                   sequence_count += 1

                if previous_count < count:
                   previous_count = count
                
        return previous_count