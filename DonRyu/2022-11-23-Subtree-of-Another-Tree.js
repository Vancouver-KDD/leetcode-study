const isSubtree = function (s, t) {
  const is = (node1, node2) => {
    if (!node1 && !node2) {
      return true
    }
    if (!node1 || !node2) {
      return false
    }
    if (node1.val !== node2.val) {
      return false
    }
    return is(node1.left, node2.left) && is(node1.right, node2.right)
  }
  const aux = node => is(node, t) || (!!node && aux(node.left, t)) || (!!node && aux(node.right, t))
  return aux(s)
}
