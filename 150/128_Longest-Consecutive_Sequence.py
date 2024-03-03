class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        if len(nums) == 0:
            return 0

        table = set(nums)

        best = 1

        for i in table:
                            # Checks whether number has no number immediately above it -- if so, starts counting down
            if i+1 not in table:
                x = 1
                            # ... checking each numbernbelow in turn
                while i-x in table:
                    x += 1
                            # and updating the record with the longest streak
                    if x > best:
                        best = x

        return(best)

if __name__ == "__main__":
    Solution.longestConsecutive(Solution,[100,4,200,1,3,2])