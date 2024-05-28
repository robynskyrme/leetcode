class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        k = len(nums)
        end = k-1

        clicker = 1

        i = 1

        while i <= end:
            print(clicker)
            if nums[i] == nums[i-1]:
                clicker += 1
            if nums[i] != nums[i-1] and clicker > 2:
                nums = self.shiftBack(self,nums,i,clicker-2)
                k -= clicker-2
                i -= clicker-2
            if nums[i] != nums[i-1]:
                clicker = 1

                            # Case for the output array ending in a string of duplicates
            # if i == k-1 and clicker > 2:
            #     k -= clicker-2

            i += 1


        print(nums)
        return k


    def shiftBack(self,nums,begin,by):
        if by <= 0:
            return nums

        length = len(nums)

        for i in range(begin,length):
            nums[i-by] = nums[i]

        return nums





if __name__ == "__main__":
    print(Solution.removeDuplicates(Solution,[1,1,1,2,2,3]))