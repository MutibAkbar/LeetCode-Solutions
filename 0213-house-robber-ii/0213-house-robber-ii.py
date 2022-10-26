class Solution:
    def helper(self, nums: List[int]) -> int:
            
        for i in range(1,len(nums)):
            if(i==1):
                if(nums[i]<nums[i-1]):
                    nums[i] = nums[i-1]
            else:
                if(nums[i]+nums[i-2] > nums[i-1]):
                    nums[i] = nums[i]+nums[i-2]
                else:
                    nums[i] = nums[i-1]
       
        return nums[-1]
    
    
    def rob(self, nums: List[int]) -> int:
        
        if(len(nums)==1):
             return nums[0]
        return max(self.helper(nums[0:-1]),self.helper(nums[1:]))