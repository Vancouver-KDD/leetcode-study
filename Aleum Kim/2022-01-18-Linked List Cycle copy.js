var hasCycle = function(head) {
   let fast = head;
   let slow = head;
   
   while(fast && fast.next) {
       slow = slow.next;
       fast = fast.next.next;
  
       
       if(fast === slow) return true;
   }
   
   return false;
};