class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        output = list()
        nums.sort()
        
        for i in range(0, len(nums)-1):
            
            if (i > 0 and nums[i] == nums[i-1]):    #skipping duplicate elements
                continue
            
            if (nums[i] > 0):                #no element less than zero as the array is sorted
                break
                
            l = i+1
            r = len(nums)-1
          
            while(l < r):
                total = nums[i] + nums[l] + nums[r]
                if(total < 0) or (l > i + 1 and nums[l] == nums[l-1]) :
                    l += 1
                elif(total > 0) or (r < len(nums) - 1 and nums[r] == nums[r+1]):
                    r -= 1
                else:
                    output.append([nums[i],nums[l],nums[r]])
                    r -= 1
                    l += 1
                        
                    
        return output
                    
                
                    
                
            