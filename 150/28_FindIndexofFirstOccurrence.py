class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """

        hlen = len(haystack)
        nlen = len(needle)


        index = -1
        found = False

        while found == False and index < hlen-nlen:
            index +=1
            slice = haystack[index:index+nlen]
            if slice == needle:
                found = True

        if found == False:
            index = -1

        return index


if __name__ == "__main__":
    print(Solution.strStr(Solution,"leetcode","leeto"))