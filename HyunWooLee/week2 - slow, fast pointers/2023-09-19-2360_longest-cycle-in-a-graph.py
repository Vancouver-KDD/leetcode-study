class Solution:
    '''

    key point:
    - at most 1 edge going out.
    - this looks like LinkedList

    steps:
    1) construct graph. Actually since index is the source of node,
    we can pretend edges list is a graph

    2) keep visited nodes, because we only need to visit one

    3) for each node, try to go through and see if they have cycle.

    eg)
    1 --> 3 --> 2
    - if we start from 1, and ends up at 2 and found out that we have no cycle,
    - then we established that 3 -> 2 is also no cycle, so we don't need to explore 3-->2 again


    then, for each node, this is essentially find a cycle in Linked list question.
    - we can use slow & fast pointer to find a cycle.
    - then finding length of circle is trivial.


    '''
    def longestCycle(self, edges) -> int:

        def get_curr_list_cycle_size(curr_node, next_node):
            slow, fast = curr_node, curr_node
            visited_items = set()

            is_cycle_detected = False
            while edges[slow] != -1 and edges[fast] != -1 and edges[edges[fast]] != -1:

                slow = edges[slow]
                fast = edges[edges[fast]]

                visited_items.add(slow)
                visited_items.add(fast)

                if slow in visited or fast in visited:
                    return 0

                if slow == fast:
                    is_cycle_detected = True
                    break

            if not is_cycle_detected:
                visited.update(visited_items)
                return 0

            # at this point we have a cycle
            curr_val = slow
            cycle_length = 0

            while True:
                slow = edges[slow]
                cycle_length += 1
                if slow == curr_val:
                    visited.update(visited_items)
                    return cycle_length

            return -1

        longest_cycle = 0
        visited = set()

        for i, child in enumerate(edges):
            if i in visited or child == -1:
                continue
            curr_list_cycle_size = get_curr_list_cycle_size(i, child)
            longest_cycle = max(longest_cycle, curr_list_cycle_size)

        return -1 if longest_cycle == 0 else longest_cycle