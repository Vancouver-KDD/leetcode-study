// class Node {
//   constructor(val, next = null, random = null) {
//       this.val = val;
//       this.next = next;
//       this.random = random;
//   }
// }

class Solution {
  /**
   * @param {Node} head
   * @return {Node}
   */
  copyRandomList(head) {
    // Node has random pointer
    // ramdom can point to any node in the list or null

    // make deep copy
    // 1. copy val
    // 2. copy next point like original next node
    // 3. copy random point like original random point
    // but don't point to original node

    // head부터 순차적으로 새로운 노드를 만들어 데이터 값을 그대로 넣는다.
    // 동시에 배열에 object형식으로 head의 노드와 새로 만들어진 노드를
    // old에 head Node를 cur에 새로 만들어진 노드를 넣는다.

    // 새로운 head Node의 random을 배열의 항목중 old와 비교하여 같은 경우 그 항목의 cur를 넣는다.

    let itemArr = [];
    let point = head;
    let newHead = new Node();
    let newPoint = newHead;

    //
    while (point) {
      let newNode = new Node(point.val);

      // 랜덤 값을 넣는다.
      itemArr.push({ old: point, cur: newNode });
      newNode.random = point.random;
      newPoint.next = newNode;
      newPoint = newPoint.next;

      point = point.next;
    }

    point = newHead.next;
    while (point) {
      itemArr.forEach((item) => {
        if (item.old == point.random) {
          point.random = item.cur;
        }
      });
      point = point.next;
    }

    return newHead.next;
  }
}
