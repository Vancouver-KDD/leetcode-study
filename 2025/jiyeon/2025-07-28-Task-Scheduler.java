class TaskScheduler {
    public int leastInterval(char[] tasks, int n) {
        int[] freq = new int[26];
        for (char c : tasks) {
            freq[c - 'A']++;
        }
        
        PriorityQueue<Integer> maxHeap = new PriorityQueue<>(Collections.reverseOrder());
        for (int f : freq) {
            if (f > 0) maxHeap.add(f);
        }

        int sequence = 0;
        while (!maxHeap.isEmpty()) {
            int interval = n + 1;
            List<Integer> remain = new ArrayList<>();
            while (interval > 0 && !maxHeap.isEmpty()) {
                int cur = maxHeap.poll();
                if (cur > 1) remain.add(cur - 1);
                sequence++;
                interval--;
            }

            for (int r : remain) {
                maxHeap.add(r);
            }

            if (!maxHeap.isEmpty()) {
                sequence += interval;
            }
        }

        return sequence;
    }
}