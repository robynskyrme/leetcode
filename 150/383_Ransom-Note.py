class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """

        possible = True

        pointer = 0

        while ransomNote:
            char = ransomNote[0]
            if magazine.count(char) == 0:
                possible = False
            else:
                i = magazine.index(char)
                magazine = magazine[:i] + magazine[i+1:]


            ransomNote = ransomNote[1:]

        return possible




if __name__ == "__main__":
    print(Solution.canConstruct(Solution,"aa","aba"))