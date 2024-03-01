class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

                            # Input is *letters only*, so if they don't match in length, they're not anagrams
        if len(s) != len(t):
            return False

                            # Initialize two empty tables
        table_s = []
        table_t = []

        for i in range(256):
            table_s.append(0)
            table_t.append(0)

                            # Use the tables to count the characters in each string
        for chars in range(len(s)):
            table_s[ord(s[chars])] += 1
            table_t[ord(t[chars])] += 1

                            # If those counting-tables match, the words are anagrams
        if table_s == table_t:
            return True
        else:
            return False



if __name__ == "__main__":
    print(Solution.isAnagram(Solution,"foxfoxfox","oxfoxfoxf"))