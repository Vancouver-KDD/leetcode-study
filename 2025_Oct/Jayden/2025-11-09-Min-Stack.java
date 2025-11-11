class MinStack {
    /**
        Time Complexity: O(1)
        Space Complexity: O(n)
     */
    private class Node {
        public int val;
        public int min;

        public Node(int val, int min) {
            this.val = val;
            this.min = min;
        }
    }

    List<Node> list = null;

    public MinStack() {
        list = new ArrayList<>();
    }

    public void push(int val) {
        if (list.isEmpty()) {
            list.add(new Node(val, val));
            return;
        }

        int min = list.get(list.size() - 1).min;
        list.add(new Node(val, Math.min(min, val)));
    }

    public void pop() {
        if (list.isEmpty())
            return;
        list.remove(list.size() - 1);
    }

    public int top() {
        if (list.isEmpty())
            return -1;
        return list.get(list.size() - 1).val;
    }

    public int getMin() {
        if (list.isEmpty())
            return -1;
        return list.get(list.size() - 1).min;
    }
}