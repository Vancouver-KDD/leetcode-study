var KthLargest = function (k, nums) {
  KthLargest.prototype.heap = buildHeap(nums);
  KthLargest.prototype.k = k;
  extract(KthLargest.prototype.k);
};

const buildHeap = (nums) => {
  let i = 1,
    j = 1,
    temp;
  const heap = [null];
  while (i <= nums.length) {
    heap[i] = nums[i - 1];
    c = i;
    p = Math.floor(c / 2);

    while (c > 1 && heap[c] < heap[p]) {
      temp = heap[p];
      heap[p] = heap[c];
      heap[c] = temp;

      c = p;
      p = Math.floor(p / 2);
    }
    i++;
  }
  return heap;
};
const insert = (val) => {
  const heap = KthLargest.prototype.heap;
  heap.push(val);
  let c = heap.length - 1;
  let p = Math.floor(c / 2);
  let temp;
  while (c > 1 && heap[c] < heap[p]) {
    temp = heap[p];
    heap[p] = heap[c];
    heap[c] = temp;
    temp = p;
    c = p;
    p = Math.floor(temp / 2);
  }
};
const extract = (k) => {
  heap = KthLargest.prototype.heap;
  let c1, c2, temp, p;

  while (k + 1 < heap.length) {
    p = 1;
    heap[p] = heap.pop();
    c1 = p * 2;
    c2 = p * 2 + 1;
    while (heap[c1] < heap[p] || heap[c2] < heap[p]) {
      if (heap[c1] < heap[c2] || heap[c2] === undefined) {
        temp = heap[c1];
        heap[c1] = heap[p];
        heap[p] = temp;
        p = c1;
      } else {
        temp = heap[c2];
        heap[c2] = heap[p];
        heap[p] = temp;
        p = c2;
      }
      c1 = p * 2;
      c2 = p * 2 + 1;
    }
  }
};
KthLargest.prototype.add = function (val) {
  insert(val);
  extract(KthLargest.prototype.k);

  return KthLargest.prototype.heap[1];
};
