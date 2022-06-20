class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        summ = list()
        for i in range(1,len(nums)+1):
            summ.append(sum(nums[0:i]))
      
        return summ  