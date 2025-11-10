class Solution(object):
    def carFleet(self, target, position, speed):
        """
        :type target: int
        :type position: List[int]
        :type speed: List[int]
        :rtype: int
        """
        cars = sorted(zip(position, speed), reverse=True)
        stack = []

        for c in cars:
            time = float(target - c[0]) / float(c[1])
            if not stack:
                stack.append(time)
            else:
                if stack[-1] < time:
                    stack.append(time)
        return len(stack)