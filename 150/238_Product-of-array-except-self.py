class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        output = []

        left_prods = []
        right_prods = []

        left = 1
        right = 1


        for i in range(len(nums)):
            left = left * nums[i]
            left_prods.append(left)

            right = right * nums[len(nums)-1-i]
            right_prods.insert(0,right)


        left_prods.append(1)
        left_prods.insert(0,1)
        right_prods.append(1)
        right_prods.insert(0,1)

        caret = 1

        while caret <= len(nums):
            output.append(left_prods[caret-1] * right_prods[caret+1])
            caret += 1

        return output


if __name__ == "__main__":
    print(Solution.productExceptSelf(Solution,[1,2,3,4]))