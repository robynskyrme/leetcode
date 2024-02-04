class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """

        output = ""

        while len(s) > 0:
            word = ""
            s = Solution.TopandTail(self,s)


            c = ""

            c = s[-1]

            while c != " " and len(s) > 0:
                word = c + word

                s = s[:-1]
                # print ("|" + s + "|")
                if s:
                    c = s[-1]


            # print(c)
            output = output + word + " "

            # print(output)

        return Solution.TopandTail(self,output)

    def TopandTail(self,s):
        while s[0] ==" ":
            s = s[1:]

        while s[-1] == " ":
            s = s[:-1]
        return s



if __name__ == "__main__":
    print(Solution.reverseWords(Solution,"  this string   to have   whitespace  removed  and the words  in it  reversed    "))