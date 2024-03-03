class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        differences = {}

        for i in range(len(nums)):
            difference = target - nums[i]
            if difference in differences:
                return [differences[difference], i]
            else:
                differences[nums[i]] = i

if __name__ == "__main__":
    print(Solution.twoSum(Solution,[4,2,7,6,3],8))