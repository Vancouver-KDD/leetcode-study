import java.util.*;

class MedianFinder {
    private PriorityQueue<Integer> small = new PriorityQueue<>(Collections.reverseOrder());
    //biggest ones among smaller ones
    private PriorityQueue<Integer> large = new PriorityQueue<>(); //smallest one among bigger ones
    private boolean even = true;

    /*Adding an element to a priority queue implemented as a binary heap 
    takes O(log n) time complexity on average. 
    The worst-case time complexity for adding an element 
    to a binary heap-based priority queue is O(n),     
    which occurs when the heap needs to be resized. */

    public MedianFinder() {        
    }
    
    public void addNum(int num) { //O(logn)
        if(even) {
            //even이면 large에 일단 넣어서 나오는 걸, small에 넣기
            large.offer(num);
            small.offer(large.poll());
        }else{
            //odd면 small에 넣고 larget에서 꺼내서 넣기
            //odd라는 건 small에 한 개 더 많다는 거
            small.offer(num);
            large.offer(small.poll());
        }
        even = !even;
    }
    
    public double findMedian() { //O(1)
        if(even) {
            return small.peek() + large.peek() / 2.0;
        }else {
            return small.peek();
        }
    }
}

/**
 * Your MedianFinder object will be instantiated and called as such:
 * MedianFinder obj = new MedianFinder();
 * obj.addNum(num);
 * double param_2 = obj.findMedian();
 */