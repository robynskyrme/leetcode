class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        sarray = []
        tarray = []

        for i in range(256):
            sarray.append(0)
            tarray.append(0)

        for char in s:
            sarray[ord(char)] += 1
        for char in t:
            tarray[ord(char)] += 1

        print(sarray)
        print(tarray)

        while sarray:
            if tarray.count(sarray[0]) == 0:
                return False
            del tarray[tarray.index(sarray[0])]
            del sarray[0]
            print(tarray)
        return True

if __name__ == "__main__":
    print(Solution.isIsomorphic(Solution,"eggk","orff"))