class TimeMap {

    /**
        Time Complexity:
            - insert: O(1)
            - retrieve: O(log(n))

        Space Complexity: O(n)
     */

    Map<String, List<Node>> map = null;

    private class Node {
        public String value;
        public int timestamp;

        public Node(String value, int timestamp) {
            this.value = value;
            this.timestamp = timestamp;
        }
    }

    public TimeMap() {
        map = new HashMap<>();
    }

    public void set(String key, String value, int timestamp) {
        List<Node> list = map.getOrDefault(key, new ArrayList<>());
        list.add(new Node(value, timestamp));
        map.put(key, list);
    }

    public String get(String key, int timestamp) {
        List<Node> list = map.get(key);

        if (list == null) return "";

        int left = 0;
        int right = list.size() - 1;
        String result = "";

        while (left <= right) {
            int mid = left + (right - left) / 2;
            Node node = list.get(mid);

            if (node.timestamp <= timestamp) {
                result = node.value;
                left = mid + 1;
            } else {
                right = mid - 1;
            }
        }

        return result;
    }
}

/**
 * Your TimeMap object will be instantiated and called as such:
 * TimeMap obj = new TimeMap();
 * obj.set(key,value,timestamp);
 * String param_2 = obj.get(key,timestamp);
 */