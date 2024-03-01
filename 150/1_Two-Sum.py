

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        sol_a = 0
        sol_b = 0

                            # Simply loop through the whole list twice, checking for correct sum
        for b in range(len(nums)):
            for a in range(len(nums)):

                sum = nums[a] + nums[b]

                            # If correct, store the results (that there is only one is given)
                            # wihle checking that a number is not being added to itself
                if sum == target and a != b:
                    sol_a = a
                    sol_b = b
                    break

        return [sol_a,sol_b]


if __name__ == "__main__":
    print(Solution.twoSum(Solution,[4,2,7,6,3],8))