class Solution:
    def asteroidCollision(self, asteroids: list[int]) -> list[int]:
        stack = [asteroids[0]]
        for current_asteroid in asteroids[1:]:
            while stack and current_asteroid < 0 and stack[-1] > 0:
                if abs(current_asteroid) > abs(stack[-1]):
                    stack.pop()
                elif abs(current_asteroid) == abs(stack[-1]):
                    stack.pop()
                    current_asteroid = 0
                    break
                else:
                    current_asteroid = 0
                    break
            if current_asteroid != 0:
                stack.append(current_asteroid)
        return stack