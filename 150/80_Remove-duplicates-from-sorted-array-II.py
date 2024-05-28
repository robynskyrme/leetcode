class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

                            # useful numbers:
                            # k is an array length which will decrease each time we remove in place
                            # end is just the last index of the *original* array (doesn't change)
        k = len(nums)
        end = k-1
                            # clicker: keeps a tally of how many IN A ROW of a certain digit
        clicker = 1

                            # loop from index 1 to the end of the original array
        i = 1

        while i <= end:
                            # if the key being looked at is the same as th previous key,
            if nums[i] == nums[i-1]:
                            # increment the clicker
                clicker += 1
                            # if the key is different (a new key) AND the clicker says there's more than 2 in a row
                            # of the previous key,
            if nums[i] != nums[i-1] and clicker > 2:
                            # then shift forward everything in the array after that point, by the relevant factor
                nums = self.shiftBack(self,nums,i,clicker-2)
                            # decrease k by the number of elements removed
                k -= clicker-2
                            # our 'cursor' must also be moved back, too, to account for removed elements
                i -= clicker-2

                            # whether or not we just had a string of elements,
                            # if the new key is different, we reset the clicker to 1
            if nums[i] != nums[i-1]:
                clicker = 1

                            # special case for the output array ending in a string of duplicates
            if i == k-1 and clicker > 2:
                k -= clicker-2

            i += 1


        print(nums)
        return k


                            # function to remove elements in place (by copying, element by element, backwards)
    def shiftBack(self,nums,begin,by):
        if by <= 0:
            return nums

        length = len(nums)

        for i in range(begin,length):
            nums[i-by] = nums[i]

        return nums



# Pausing for today
# Numbers given in example are the Leetcode test which it fails -- output array is correct, but k is too small by one (!)

if __name__ == "__main__":
    print(Solution.removeDuplicates(Solution,[-50,-49,-48,-47,-46,-46,-45,-44,-43,-43,-42,-41,-41,-41,-40,-40,-40,-39,-38,-38,-38,-38,-38,-38,-37,-35,-35,-35,-35,-34,-33,-33,-31,-31,-30,-29,-29,-28,-28,-28,-28,-28,-27,-27,-27,-26,-26,-25,-25,-25,-25,-24,-24,-23,-23,-23,-21,-21,-20,-20,-20,-18,-17,-17,-16,-16,-16,-15,-15,-14,-13,-13,-12,-12,-11,-11,-10,-10,-9,-8,-8,-7,-7,-6,-6,-6,-5,-3,-2,-2,-1,-1,-1,0,0,0,1,2,2,3,3,3,3,4,4,6,6,7,8,9,9,9,9,10,10,10,11,11,11,11,11,11,12,14,15,15,17,17,18,19,19,20,20,20,20,21,21,21,23,23,24,24,25,25,25,25,26,26,27,27,28,28,29,31,31,33,34,34,35,35,36,37,37,37,39,39,40,41,41,41,42,42,42,45,46,47,49]))