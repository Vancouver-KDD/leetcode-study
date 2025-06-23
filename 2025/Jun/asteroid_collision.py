class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for asteroid in asteroids:
            while stack and asteroid < 0 < stack[-1]:
                gap = stack[-1] + asteroid
                if gap < 0:
                    stack.pop()
                    continue
                elif gap is 0:
                    stack.pop()
                break
            else:
                stack.append(asteroid)
        return stack