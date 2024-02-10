class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """



        s = self.alphanumOnly(Solution,s)

        a = ""
        b = ""

        while s:
            a = s[0]
            b = s[-1]
            print(a)
            print(b)

            if a != b:
                return False

            if len(s) > 2:
                s = s[1:-1]
            else:
                s = ""

        return True



    def alphanumOnly(self,raw):
        output = ""

        for char in raw:
            if Solution.isalphanum(Solution,char):
                if Solution.isUppercase(Solution,char):
                    char = Solution.makeLowercase(Solution,char)
                output += char

        return output


    def isalphanum(self,char):

        asc = ord(char)

        if asc > 47 and asc < 58:
            return True

        if asc < 65 or asc > 122:
            return False
        if asc > 90 and asc < 97:
            return False

        return True


    def makeLowercase(self,char):
        char = chr(ord(char) + 32)
        return char

    def isUppercase(self,char):
        if ord(char) < 97:
            return True
        return False


if __name__ == "__main__":
    print(Solution.isPalindrome(Solution,"0P"))