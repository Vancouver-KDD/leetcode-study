
# hash set => o(n), o(n) 
def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        hash_set = set()

        while head:

            if head in hash_set:
                return head
            hash_set.add(head)
            head = head.next

        return None    


# hare and tortoise => o(n), o(1)
class ListNode:
    def __init__(self, val=0):
        self.val = val
        self.next = None

def detectCycle(head):
    slow = head
    fast = head
    
    # 플로이드의 토끼와 거북이 알고리즘을 사용하여 사이클 검출
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            
            break
    
    # 사이클이 없는 경우
    if not fast or not fast.next:
        return None
    
    # 사이클이 있는 경우, 시작 노드를 찾는 과정
    slow = head
 
    while slow != fast:
        slow = slow.next
        fast = fast.next
    
    return slow

# 예제 입력 생성
head = ListNode(3)
head.next = ListNode(2)
head.next.next = ListNode(0)
head.next.next.next = ListNode(-4)
head.next.next.next.next = head.next  # 사이클 설정

result = detectCycle(head)
if result:
    print("사이클이 시작하는 노드의 값:", result.val)
else:
    print("사이클이 없습니다.")