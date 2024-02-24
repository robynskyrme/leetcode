
class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        table = []

                            # Initialize an empty table to represent every ascii character
        for i in range(256):
            table.append(None)

                            # For every character in s, assign the matching character in t to s's slot in the table
        for char in range(len(s)):
                            # (assuming the slot is empty)
            if not table[ord(s[char])]:
                table[ord(s[char])] = t[char]
            else:
                            # ... if it isn't empty, make sure that what's there matches the character in s
                if table[ord(s[char])] != t[char]:
                            # because if not, it's a failure
                    return False

                            # Check that no character is mapped to twice
            if table.count(t[char]) > 1:
                    return False

                            # All this being okay, simply return true
        return True


if __name__ == "__main__":
    print(Solution.isIsomorphic(Solution,"badc","baba"))