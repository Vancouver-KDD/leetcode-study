/**
 * Definition for singly-linked list.
 * class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) {
 *         val = x;
 *         next = null;
 *     }
 * }
 */

//HashSet 이용 
//limitation: Do not modify the linked list.
//Time Complexity: O(N)
//Space Complexity: O(N)
/*
public class Solution {
    public ListNode detectCycle(ListNode head) {
        if(head == null || head.next == null){
            return null;
        }

        Set<ListNode> visited = new HashSet<>();
        ListNode checkNode = head;
        while(checkNode != null){
            if(visited.contains(checkNode)){
                return checkNode;
            }

            visited.add(checkNode);
            checkNode = checkNode.next;
        }

        return null;
    }
}
*/
//leetcode 의 fast -slow 방식 사용 ( with floyd's cycle algorithm)
//Time Complexity: O(N)
//Space Complexity: O(1)
public class Solution {
    public ListNode detectCycle(ListNode head) {

        ListNode fast = head;
        ListNode slow = head;

        // Move slow - one step and fast- two steps
        while(fast != null && fast.next != null){
            fast = fast.next.next;
            slow = slow.next;
            
            // Check if the hare meets the tortoise
            if(fast == slow){
                break;
            }
        }
        // Check if there is no cycle
        if(fast == null || fast.next == null){
            return null;
        }

        // Reset either tortoise or hare pointer to the head
        fast = head;
         // Move both pointers one step until they meet again
        while(fast != slow){
            fast = fast.next;
            slow = slow.next;
        }
         // Return the node where the cycle begins
        return fast;

    }
}

/*
[알고리즘 설명] 
경우에 따라서는 fast 가 1번 cycle 이 아니라 여러 cycle 돌다가 slow 를 만나기도 한다. 
그리고 fast 를 만나게 되는 slow 의 이동 step 은  늘 ( step 수 <= N ) 을 만족.
=> [설명] slow 는 floyd cycle algorithm 공식의 증명을 보면 알듯이 cycle 이 max size 인경우 
(tail 이 head 를 point 하는경우)  list 개수 = n 번 이동후 fast/slow 가 처음. 만난다. 
만약 tail 이 중간 node 를 pointing 하는 경우는 cycle 이 작아지고, n번 보다 작게 이동후 만난다. 
 

ex) 0->1->2->3->4->5->6->7->8->9  의 리스트이고 9는 6으로 돌아가는 cycle 이라고 한다면
    slow: 0->1->2->3->4->5->6->7->8->9
    fast: 0->2->4->6->8->6->8->6->8  (cycle 2바퀴 돌고 3바퀴째에 slow 와 만남)

    - cycle 회전수를 임의의 k 라고 하고  (<- list cycle 모양에 따라 다르게 되므로.)
    - head 부터 cycle 이 시작되는 node 6 까지 길이 = a (위 예제에서는 6)
    - cycle 시작되는 node 6부터 처음으로 fast/slow 가 만나는 node 8 까지의 길이 = b (위예제-2)
    - cycle 시작되는 node 6부터 사이클이 끝나는 node 9 까지의 길이 = c (위예제-4)

    fast 가 (a + k*c + b) 이동후 (a+b) 이동한 slow 를 만남. fast 는 slow 보다 2배이동했으므로 
    (a + k*c + b) = 2* (a +b) 가 성립
    k*c = a + b  
    fast 와 slow 가 만난뒤 (cycle 상에서 b 위치) => fast 를 head 로 위치를 옮기고 fast 와 slow 둘다 1 step 씩 a 번을 이동하면 fast 와 slow 는 cycle 시작점에서 다시 만난다. 
    즉,fast 는 cycle 상에서 b 위치에 있는데 이 위치에서 a 만큼 더 이동하면, 적게는 1바퀴(k=1), 또는 여러 바퀴 cycle 돈후에 cycle 시작점에서 slow 와 만나게 되는 것임. 
    
*/
/*
위 설명이 헷갈리면 아래 설명으로 이해하고 다시 위의것을 보면 잘 이해가 됨. 
아래 설명은 fast 가 1바퀴 cycle 만에 바로 slow 를 만난경우이고, 변수도 x1 (=a), x2(=b), x3 (x2+x3 = C) 를 가지고 설명함. 
- head부터 cycle 시작점까지 길이:x1
- cycle 시작점부터 slow 와 fast 가 만난점까지 길이 : x2
- fast/slow 만난점부터 cycle 시작점까지 길이: x3
[Let's Do some math work. To understand this solution, you just need to ask yourself this question.]
Assume the distance from head to the start of the loop is x1
the distance from the start of the loop to the point fast and slow meet is x2
the distance from the point fast and slow meet to the start of the loop is x3
What is the distance fast moved? What is the distance slow moved? And their relationship?
=> x1 + x2 + x3 + x2 = 2 (x1 + x2)  => Therefore, x1 = x3.
Ans: Its just the relationship between the distance travelled by fast pointer and the distance travelled by the slow pointer.
As fast pointer, runs twice the speed of slow pointer. Therefore, when they meet, distance travelled by fast pointer will be 2*(distance travelled by slow pointer).
*/
