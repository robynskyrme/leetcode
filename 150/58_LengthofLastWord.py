# leetcode

class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """

                            # Remove trailing whitespace
        while s[len(s)-1] == " ":
            s = s[:-1]

        if s.count(" ") == 0:
            return len(s)
                            # Count backwards til there's a space
        length = 0
        while s[len(s)-length-1] != " ":
            length += 1

        return length


if __name__ == "__main__":
    print(Solution.lengthOfLastWord(Solution,"a"))