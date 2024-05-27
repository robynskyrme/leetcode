# It didn't say you COULDN'T just treat it as a string.....

class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """

        string = str(x)

        while len(string) > 1:
            if string[0] == string[len(string)-1]:
                string = string[1:]
                string = string[:-1]
            else:
                return False

        return True

if __name__ == "__main__":
    print(Solution.isPalindrome(Solution,78787))