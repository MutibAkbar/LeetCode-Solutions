class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        one = cost[-2]
        two = cost[-1]
        
        for i in range(len(cost)-3,-1,-1):
            cost[i] = cost[i] + min(one,two)
            temp = one
            one = cost[i]
            two = temp
            
        return min(cost[0],cost[1])
            
      
        