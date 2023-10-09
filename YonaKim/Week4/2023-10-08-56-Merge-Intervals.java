import java.util.Arrays;
import java.util.LinkedList;

/**
Time Complexity: O(nlogn)
For LinkedList<E>

- get(int index) is O(n) (with n/4 steps on average), but O(1) when index = 0 or index = list.size() - 1 (in this case, you can also use getFirst() and getLast()). One of the main benefits of LinkedList<E>
- add(int index, E element) is O(n) (with n/4 steps on average), but O(1) when index = 0 or index = list.size() - 1 (in this case, you can also use addFirst() and addLast()/add()). One of the main benefits of LinkedList<E>
- remove(int index) is O(n) (with n/4 steps on average), but O(1) when index = 0 or index = list.size() - 1 (in this case, you can also use removeFirst() and removeLast()). One of the main benefits of LinkedList<E>
- Iterator.remove() is O(1). One of the main benefits of LinkedList<E>
- ListIterator.add(E element) is O(1). One of the main benefits of LinkedList<E>
- Note: Many of the operations need n/4 steps on average, constant number of steps in the best case (e.g. index = 0), and n/2 steps in worst case (middle of list)

For ArrayList<E>

- get(int index) is O(1). Main benefit of ArrayList<E>
- add(E element) is O(1) amortized, but O(n) worst-case since the array must be resized and copied
- add(int index, E element) is O(n) (with n/2 steps on average)
- remove(int index) is O(n) (with n/2 steps on average)
- Iterator.remove() is O(n) (with n/2 steps on average)
- ListIterator.add(E element) is O(n) (with n/2 steps on average)

Space Complexity: O(logN)
*/
class Solution {
    public int[][] merge(int[][] intervals) {
        LinkedList<int[]> result = new LinkedList<>();

        //Arrays.sort(intervals, Comparator.comparingInt(x -> x[0]));
        Arrays.sort(intervals, (x,y) -> Integer.compare(x[0],y[0]));

        for(int[] interval : intervals) {
            if(result.isEmpty() || result.getLast()[1] < interval[0]) {
                //if there is no overlap, add interval to result
                result.add(interval);
            } else {
                //if there is overlap, merge interval into last element in result
                result.getLast()[1] = Math.max(result.getLast()[1], interval[1]);
            }
        }

        return result.toArray(new int[result.size()][]);
    }
}