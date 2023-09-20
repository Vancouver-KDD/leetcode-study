class Solution:
    '''
    Step 1:
    - because each node has at most 1 edge, we can think of this like a linked list
    - for each node, traverse "linked-list" and find longest cycle

    - we expect O(n^2) run time, if we traverse linked list for each node.
    '''
    def longestCycleV1(self, edges) -> int:

        def get_curr_list_cycle_size(node):
            return -1

        longest_cycle = 0
        for i in range(len(edges)):
            curr_list_cycle_size = get_curr_list_cycle_size(i)
            longest_cycle = max(longest_cycle, curr_list_cycle_size)
        return -1 if longest_cycle == 0 else longest_cycle

    '''
    Step 2:
    - for each node, we find if cycle exists.
    - if cycle exists, then we can easily get the length of cycle by traversing the cycle once.
    - the idea is same as finding cylce in linked list, using slow and fast pointer.
    - in this problem, NULL is equivalent of node pointing to -1
    
    runtime: O(n^2)
    space: O(1)
    
    TLE on large output
    '''
    def longestCycleV2(self, edges) -> int:

        def get_curr_list_cycle_size(curr_node):
            slow, fast = curr_node, curr_node

            is_cycle_detected = False
            '''
            This is exactly the same idea as typical Linked list cycle problem
            
            while slow and fast and fast.next:
               slow = slow.next
               fast = fast.next.next
               ...
            '''
            while edges[slow] != -1 and edges[fast] != -1 and edges[edges[fast]] != -1:

                slow = edges[slow]
                fast = edges[edges[fast]]

                if slow == fast:
                    is_cycle_detected = True
                    break

            if not is_cycle_detected:
                return 0

            # at this point we have a cycle
            curr_val = slow
            cycle_length = 0

            # if we have cycle, calculate length
            while True:
                slow = edges[slow]
                cycle_length += 1
                if slow == curr_val:
                    return cycle_length

            return -1

        longest_cycle = 0
        for i, child in enumerate(edges):
            curr_list_cycle_size = get_curr_list_cycle_size(i)
            longest_cycle = max(longest_cycle, curr_list_cycle_size)
        return -1 if longest_cycle == 0 else longest_cycle

    '''
    Step 3:
    Optimization
    - how do we reduce runtime?
    - consider this example
    200 --> 150 --> (100 more items in between) --> 1
    
    Step A:
    To find if 200 has a cycle, you need to go through 103 nodes
     - I will need to go thorugh 103 items
     
     Step B:
     To find if 150 has a cycle, you need to go through 102 nodes.
     - But do you really need to? No since in step A, I already visited 150, so I don't need to visit it again.
     - So, that means it only takes 2 steps to find out 150 is not a cycle
    
    Then, we can store visited items, so we dont go through same items multiple times
    '''

    def longestCycle(self, edges) -> int:

        def get_curr_list_cycle_size(curr_node):
            slow, fast = curr_node, curr_node

            '''
            Why do I need to have visited_items, and visited set? 
            Because to find linked list, I will need to revisit same nodes again.
            '''
            visited_items = set()

            is_cycle_detected = False
            while edges[slow] != -1 and edges[fast] != -1 and edges[edges[fast]] != -1:

                slow = edges[slow]
                fast = edges[edges[fast]]

                visited_items.add(slow)
                visited_items.add(fast)

                # if previous get_curr_list_cycle_size stored these nodes, then we terminate immediately
                # see my comment on Step A, Step B
                if slow in visited or fast in visited:
                    return 0

                if slow == fast:
                    is_cycle_detected = True
                    break

            if not is_cycle_detected:
                # see comment on Step A, Step B
                visited.update(visited_items)
                return 0

            # at this point we have a cycle
            curr_val = slow
            cycle_length = 0

            while True:
                slow = edges[slow]
                cycle_length += 1
                if slow == curr_val:
                    # see comment on Step A, Step B
                    visited.update(visited_items)
                    return cycle_length

            return -1

        longest_cycle = 0
        visited = set()

        for i, child in enumerate(edges):
            if i in visited:
                continue
            curr_list_cycle_size = get_curr_list_cycle_size(i, child)
            longest_cycle = max(longest_cycle, curr_list_cycle_size)

        return -1 if longest_cycle == 0 else longest_cycle