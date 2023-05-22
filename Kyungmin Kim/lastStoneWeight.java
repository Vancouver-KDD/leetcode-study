class Solutiion {
    public int lastStoneWEight(int[] stones) {
        PriorityQueue<Integer> maxHeap = new PriorityQueue();
        for (int stone : stones) max.Heap.add(-stone);
        while(maxHeap.size() >1){
            int stone1 = maxHeap.remove();
            int stone2 = maxHeap.remove();
            if (stone1 != stonbe2) maxHeap.add(stone1 - stone2);
        }
        return maxHeap.size() != 0 ? (-maxHeap.remove()) : 0;
    }
}