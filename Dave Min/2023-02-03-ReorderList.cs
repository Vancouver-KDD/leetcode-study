/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     public int val;
 *     public ListNode next;
 *     public ListNode(int val=0, ListNode next=null) {
 *         this.val = val;
 *         this.next = next;
 *     }
 * }
 */
public class Solution
{
    public void ReorderList(ListNode head)
    {
        ListNode root = head;
        List<int> list = new List<int>();
        while (root != null)
        {
            list.Add(root.val);
            root = root.next;
        }
        root = head;
        for (int i = 0; i < list.Count; i++)
        {
            if (i % 2 == 0)
                root.val = list[i / 2];
            else
                root.val = list[list.Count - 1 - i / 2];
            root = root.next;
        }

    }
}