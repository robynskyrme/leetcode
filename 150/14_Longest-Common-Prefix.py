class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """

        alphacount = []
        for i in range (26):
            alphacount.append(0)

        temp = ""



        print(temp)

        prefix = ""

        while strs:
            print(temp)
            temp = ""

            for each in strs:
                temp += each[0]

            for i in range(len(strs)):
                if temp.count(strs[i][0]) == 1:
                    del strs[i]



            print(prefix)


        print(strs)

if __name__ == "__main__":
    Solution.longestCommonPrefix(Solution,["ddog","dracecar","dcar","hazd"])