class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        cars = sorted(zip(position, speed))
        car_stack = []
        no_of_fleets = 0
        max_time = 0

        for i in range(len(cars) - 1, -1, -1):
            time = (target - cars[i][0]) / cars[i][1]

            if time > max_time:
                no_of_fleets += 1
                max_time = time

        return no_of_fleets
            
            
            
            
        