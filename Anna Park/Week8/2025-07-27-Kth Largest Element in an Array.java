class FindKthLargest {
    public int findKthLargest(int[] nums, int k) {

        PriorityQueue<Integer> pq = new PriorityQueue<>();

        //min heap
        for(int x: nums){
            pq.add(x);
        }

        System.out.println(pq);

        for(int i=0; i<k-1; i++){
            pq.poll();
        }

        return pq.poll();
    }
}