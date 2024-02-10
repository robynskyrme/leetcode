class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """

        if len(s) < 2:
            return False
        if len(s) % 2 == 1:
            return False

        parens_o = ["(","{","["]
        parens_c = [")","}","]"]

        parenstack = [0]

        for char in s:
            if parens_o.count(char) == 1:
                parenstack.insert(0,parens_o[parens_o.index(char)])
            if parens_c.count(char) == 1:

                if parenstack[0] != parens_o[parens_c.index(char)]:
                    return False
                if parenstack[0] == parens_o[parens_c.index(char)]:
                    del parenstack[0]

        if parenstack == [0]:
            return True
        else:
            return False


if __name__ == "__main__":
    print(Solution.isValid(Solution,"))"))