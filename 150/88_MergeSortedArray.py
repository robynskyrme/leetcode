class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """

        for item2 in nums2:
            index = 0

            while nums1[index] > 0 and item2 > nums1[index]:
                index += 1

            nums1.insert(index,item2)
            del nums1[-1]


if __name__ == "__main__":
    Solution.merge(Solution,[3,6,5,2,6,4,0,0,0,0],6,[1,0,2,6], 4)