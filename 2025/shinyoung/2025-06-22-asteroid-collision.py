def asteroidCollision(asteroids):
    stack = []
    for a in asteroids:
        alive = True
        while alive and stack and stack[-1] > 0 and a < 0:
            if stack[-1] < -a:
                stack.pop()
                continue
            elif stack[-1] == -a:
                stack.pop()
            alive = False
        if alive:
            stack.append(a)
    return stack


print(asteroidCollision([5, 10, -5]))
print(asteroidCollision([8, -8]))
print(asteroidCollision([10, 2, -5]))
