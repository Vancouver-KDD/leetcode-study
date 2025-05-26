## Approach
- Think from each course's perspective, and create a hashmap for the prerequisites of each course first.
- Iterate each course with depth first search, and in the dfs, iterate the prerequisites with dfs.
  - If the most down prerequisites are empty then the course is takable
  - Also maintain the visited set, to be more efficient, and if in the visited set, don't repeat and return early.
  - At the end of each iteration, clean up the visited set and prerequisites map 

### Complexity
- Time complexity - O(N + P), while n is the number of the courses and P is the number of the prerequisites. P is the number of edges
- Space complexity - O(N + P)

### Solution
```
# @param {Integer} num_courses
# @param {Integer[][]} prerequisites
# @return {Boolean}
def can_finish(num_courses, prerequisites)
    return true if prerequisites.empty?

    # Create a prerequsite map for each course
    @pre_map = Hash.new([])
    for i in 0..(num_courses - 1) do
        @pre_map[i] = []
    end

    for prerequisite in prerequisites do
        @pre_map[prerequisite[0]] << prerequisite[1]
    end

    # Will iterate the list by course. Then check if the prerequisite can be completed by dfs
    @visited = Set.new
    for course in 0..(num_courses - 1) do
       return false unless dfs(course)
    end

    true
end

private def dfs(course)
    return true if @pre_map[course].empty?
    return false unless @visited.add?(course)

    for pre in @pre_map[course] do
        return false unless dfs(pre)
    end
    
    @visited.delete(course)
    @pre_map[course] = []

    true
end
```
