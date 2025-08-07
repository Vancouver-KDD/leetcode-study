```
class Solution {
    public int leastInterval(char[] tasks, int n) {
        // 1. Count frequencies of each task (A–Z)
        int[] freq = new int[26];
        for (char t : tasks) {
            freq[t - 'A']++;
        }

        // 2. Find the maximum frequency
        int maxFreq = 0;
        for (int f : freq) {
            maxFreq = Math.max(maxFreq, f);
        }

        // 3. Count how many tasks have the maximum frequency
        int countMax = 0;
        for (int f : freq) {
            if (f == maxFreq) {
                countMax++;
            }
        }

        // 4. Calculate parts and the minimum length with idle slots
        int parts = maxFreq - 1;
        int slots = parts * (n + 1) + countMax;

        // 5. The result is the larger of slots needed or total tasks
        return Math.max(tasks.length, slots);
    }
}

```
