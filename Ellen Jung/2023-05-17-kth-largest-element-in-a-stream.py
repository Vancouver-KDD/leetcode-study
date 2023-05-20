class KthLargest(object):

    def __init__(self, k, nums):
        """
        :type k: int
        :type nums: List[int]
        """
        self.k = k
        self.nums = nums

    def add(self, val):
        """
        :type val: int
        :rtype: int
        """
        self.nums.append(val)
        self.nums.sort(reverse=True)

        return self.nums[self.k - 1]

def main():
    kthLargest = KthLargest(3, [4, 5, 8, 2]);
    kthLargest.add(3);
    kthLargest.add(5);
    kthLargest.add(10);
    kthLargest.add(9);
    kthLargest.add(4);


if __name__ == '__main__':
    main()