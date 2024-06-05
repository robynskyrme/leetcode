class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

                            # If there are no zeroes in the sequence, game will always be possible
                            # For those sequences where zeroes exist, store them in an array
        zeroes = [0]
        for i in range(len(nums)):
            if nums[i] == 0:
                            # Should there be a string of consecutive zeroes, only deal with the last one
                if zeroes[len(zeroes)-1] == i-1:
                    zeroes[len(zeroes)-1] += 1
                else:
                            # Either way, store the zero's position
                    zeroes.append(i)
        if zeroes[0] == 0:
            zeroes.pop(0)
                            # If there ARE no zeroes (or the array is only 1 number) the game must be possible
        if not zeroes or len(nums) == 1:
            return True

        print(zeroes)

                            # Variable to store the indexes of the last problem area that we've shown can be solved
        passed = -1

        while zeroes:
            c = zeroes[0]

                            # For each zero, check to see whether any number prior to it can skip over it
            escape = False
            for j in range(passed+1,c):
                distance = c-j
                print("Distance: " + str(distance) + "       passed: " + str(passed) + "     j: " + str(j))
                if distance % nums[j] > 0:
                    escape = True
                print(escape)

            if escape == False:
                return False

            passed = zeroes[0]

            zeroes.pop(0)

        return True

if __name__ == "__main__":

    print(Solution.canJump(Solution,[2,0,0]))