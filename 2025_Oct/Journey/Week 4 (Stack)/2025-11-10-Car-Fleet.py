class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # Make a list of cars, where each car is represented as (position, time_to_reach_target)
        # time = (distance left) / speed
        cars = [(position[i], (target - position[i]) / speed[i]) for i in range(len(position))]

        # Sort the cars by position, starting from the car closest to the target
        cars.sort(key=lambda x: x[0], reverse=True)

        # Use a stack to keep track of car fleets
        stack = []

        # Go through each car in order (from closest to farthest)
        for i in range(len(position)):
            # If the current car reaches the target earlier or at the same time as the fleet in front,
            # it joins that fleet (so we don’t add it to the stack)
            if stack and cars[i][1] <= stack[-1][1]:
                continue
            else:
                # Otherwise, this car forms a new fleet
                stack.append(cars[i])

        # The number of fleets is the number of elements in the stack
        return len(stack)
