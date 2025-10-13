class taskScheduler {
    public int leastInterval(char[] tasks, int n) {

        int[] char_map = new int[26];
        for(int c: tasks){
            char_map[c-'A']++;
        }

        Arrays.sort(char_map);
        int max_val = char_map[25]-1;
        int idle_slots = max_val  * n;

        for(int i=24; i>=0; i--){
            idle_slots -= Math.min(char_map[i], max_val);
        }

        return idle_slots > 0 ? tasks.length + idle_slots : tasks.length;
        
    }
}