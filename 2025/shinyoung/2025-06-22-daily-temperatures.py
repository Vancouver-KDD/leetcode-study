def dailyTemperatures(temperatures):
    n = len(temperatures)
    answer = [0] * n
    stack = []

    for i, temp in enumerate(temperatures):
        while stack and temp > temperatures[stack[-1]]:
            prev_i = stack.pop()
            answer[prev_i] = i - prev_i
        stack.append(i)

    return answer


# print(dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73]))
# print(dailyTemperatures([30, 40, 50, 60]))
# print(dailyTemperatures([30, 60, 90]))
# print(dailyTemperatures([55, 38, 53, 81, 61, 93, 97, 32, 43, 78]))
# print(dailyTemperatures([93, 97, 32, 43, 78]))
print(dailyTemperatures([100,  90,  80,  70,  60]))
