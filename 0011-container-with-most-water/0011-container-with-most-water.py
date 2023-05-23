class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        left = 0 
        right = len(height) - 1
        area = 0
        water_level = 0
        
        while(left < right):
            
            if(height[left] < height[right]):
                water_level = height[left] * (right - left)
                left += 1
            else:
                water_level = height[right] * (right - left)
                right -= 1
                
            if(area < water_level):
                    area = water_level
                
                
        return area
            