from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # if a node is 1, increase the number of island and visit left, right , up, down
        # if it is 0, move to the next node
        # if the visited land is 1, mark as 0 and visit left, right , up, down
        # if it is 0, stop
        m = len(grid)
        n = len(grid[0])
        
        def visit_adjacent(cur_m, cur_n):
            coord = [(0,-1),(-1,0),(0,1),(1,0)]
            for c in coord:
                adjacent_coord = (cur_m + c[0], cur_n + c[1])
                if adjacent_coord[0] >= 0 and adjacent_coord[1] >= 0 and adjacent_coord[0] < m and adjacent_coord[1] < n:
                    # if the visited land is 1, mark as 0 and visit left, right , up, down
                    if grid[adjacent_coord[0]][adjacent_coord[1]] == "1":
                        grid[adjacent_coord[0]][adjacent_coord[1]] = "0"
                        visit_adjacent(adjacent_coord[0], adjacent_coord[1])


        island = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    island += 1
                    grid[i][j] = "0"
                    visit_adjacent(i,j)

        return island
    
grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return None
        old2new = {}
        init_node = Node(node.val)
        old2new[node] = init_node
        q = collections.deque([node])
        while q:
            cur_node = q.popleft()
            neighbor_nodes = cur_node.neighbors
            for neighbor_node in neighbor_nodes:
                # if the neighbor is not visited creat and connect
                if neighbor_node not in old2new:
                    q.append(neighbor_node)
                    new_node = Node(neighbor_node.val)
                    old2new[neighbor_node] = new_node
                    # add the new node to the cloned graph
                    old2new[cur_node].neighbors.append(new_node)
                if old2new[neighbor_node] not in old2new[cur_node].neighbors:
                    old2new[cur_node].neighbors.append(old2new[neighbor_node])
        return init_node


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        def detect_cyle(course, visited_set):
            if course not in self.pre_list:
                return False
            if course in visited_set:
                return True

            visited_set.add(course)
            for prerequisite in self.pre_list[course]:
                if detect_cyle(prerequisite, visited_set):
                    return True
            visited_set.remove(course)
            return False
        

        self.pre_list = {}
        for c, p in prerequisites:
            if c not in self.pre_list:
                self.pre_list[c] = [p]
            else:
                self.pre_list[c].append(p)
        
        for course in self.pre_list.keys():
            visited_set = set()
            if detect_cyle(course, visited_set):
                return False

        return True
            
num_course = 7

class Solution:
    def numberOfConnectedComponent(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        node_map = {}
        island = 0
        visited = set()
        
        # dfs adjacent nodes and mark them as visited
        def visit_island(node):
            if node not in visited:
                visited.add(node)
                for neighbor_node in node_map[node]:
                    visit_island(neighbor_node)
        
        for a, b in prerequisites:
            if a in node_map:
                node_map[a].append(b)
            else:
                node_map[a] = [b]
            if b in node_map:
                node_map[b].append(a)
            else:
                node_map[b] = [a]
                
        for node in node_map.keys():
            if node not in visited:
                island += 1
                visit_island(node)
        
        return island
    
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # Check for an empty graph.
        if not heights:
            return []

        p_visited = set()
        a_visited = set()
        
        rows, cols = len(heights), len(heights[0])
        directions = ((0, 1), (0, -1), (1, 0), (-1, 0))      
     
        def traverse(i, j, visited):
            if (i, j) in visited:
                return
            visited.add((i, j))
            # Traverse neighbors.
            for direction in directions:
                next_i, next_j = i + direction[0], j + direction[1]
                if 0 <= next_i < rows and 0 <= next_j < cols:
                    # Add in your question-specific checks.
                    if heights[next_i][next_j] >= heights[i][j]:
                        traverse(next_i, next_j, visited)

        for row in range(rows):
            traverse(row, 0, p_visited)
            traverse(row, cols - 1, a_visited)

        for col in range(cols):
            traverse(0, col, p_visited)
            traverse(rows - 1, col, a_visited)

        return list(p_visited & a_visited)