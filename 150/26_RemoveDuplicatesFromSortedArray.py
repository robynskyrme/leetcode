class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        print(nums)

        for index in range(len(nums)):
            if nums.count(nums[index]) > 1:
                del nums[index]
                nums.append(0)

        k = len(nums)

        print(nums)

        return k



if __name__ == "__main__":
    Solution.removeDuplicates(0,[1,1,2])