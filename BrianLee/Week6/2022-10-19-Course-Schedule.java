class Solution {
    public boolean canFinish(int numCourses, int[][] prerequisites) {
        Map<Integer, Set<Integer>> childrens = new HashMap<>();
        Map<Integer, Set<Integer>> parents = new HashMap<>();

        Queue<Integer> noChildren = new LinkedList<>();

        for(int[] pre : prerequisites) {
            childrens.computeIfAbsent(pre[1], a -> new HashSet<>()).add(pre[0]);
            parents.computeIfAbsent(pre[0], a -> new HashSet<>()).add(pre[1]);
        }

        for(int i = 0; i < numCourses; i++) {
            if(!childrens.containsKey(i)) noChildren.add(i);
        }
        int count = 0;
        while (!noChildren.isEmpty()) {
            int noChild = noChildren.poll();
            count++;

            if(parents.containsKey(noChild))
                for(int parent : parents.get(noChild)) {
                    Set<Integer> child = childrens.get(parent);
                    if(child.contains(noChild)) child.remove(noChild);
                    if(child.size() == 0) noChildren.add(parent);
                }
        }

        return count == numCourses;
    }
}