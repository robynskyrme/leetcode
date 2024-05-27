class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        stack = []
        for letter in s:
            stack.append(letter)

        for letter in t:
            if not stack:
                return True
            else:
                if letter == stack[0]:
                    stack.pop(0)

        if not stack:
            return True
        else:
            return False



if __name__ == "__main__":
    print(Solution.isSubsequence(Solution,"abc","ahbgdc"))