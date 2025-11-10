class Solution(object):
    def carFleet(self, target, position, speed):
        pair = [[pos, sp] for pos, sp in zip(position, speed)]
        stack = []

        for pos, sp in sorted(pair)[::-1]:  # reverse sorted order
            stack.append((target - pos) / float(sp))  # figure out time to reach target and add it on top of the stack
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()  # we don't need while loop here since we started from back and might have already figured that out

        return len(stack)



