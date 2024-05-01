class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        output = []
        for i in range(len(nums)):
            output.append(1)

                            # This works, but it isn't O(n)

        for i in range(len(nums)):
            for j in range(len(output)):
                if i != j:
                    output[j] = output[j] * nums[i]

        return output


if __name__ == "__main__":
    print(Solution.productExceptSelf(Solution,[1,2,3,4]))