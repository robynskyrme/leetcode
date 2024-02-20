letter_data = []

class Solution(object):

    def __init__(self):
        for j in range(10):
            letter_data.append(None)

                            # Store the keypad data in an array with index as the number
        letter_data[2] = ["a","b","c"]
        letter_data[3] = ["d","e","f"]
        letter_data[4] = ["g","h","i"]
        letter_data[5] = ["j","k","l"]
        letter_data[6] = ["m","n","o"]
        letter_data[7] = ["p","q","r","s"]
        letter_data[8] = ["t","u","v"]
        letter_data[9] = ["w","x","y","z"]


    def letterCombinations(self, digits):
        if not digits:
            return []

                            # Start with 1
        outputlist = [""]
        templist = []

                            # Strip it to digits only
        digits = Solution.Digits2to9Only(digits)

                            # For every digit given....
        for place in range(len(digits)):
                            # make a new list...
            newlist = []
            for s in outputlist:
                            # And for every combination already stored, make multiple copies of that combination
                            # -- one each for each letter possible from the current keypress
                for add in range(len(letter_data[int(digits[place])])):
                    newlist.append(s + letter_data[int(digits[place])][add])

                            # And add that to the parent list
            for copy in newlist:
                outputlist.append(copy)


                            # Since the above just copies every combination as it goes, every step of the way...
        tidylist = []
        for e in range(len(outputlist)):
                            # tidy up by deleting any which are not the same length as the given digit-string
            if len(outputlist[e]) == len(digits):
                tidylist.append(outputlist[e])

        outputlist = tidylist

        print(outputlist)
        return outputlist


                            # function to strip all chars except digits 2-9
    def Digits2to9Only(self, string):
        digitstring = ""
        for c in range(len(string)):
                            # verify by ASCII code that they're among digits 2-9; ignore any other character
            if ord(string[c]) > 49 and ord(string[c]) < 58:
                digitstring += string[c]
        return digitstring



if __name__ == "__main__":
    Solution = Solution()
    Solution.letterCombinations("23273")