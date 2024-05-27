class Solution(object):
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """

        s = s.split(" ")

                            # If they're different lengths, an obvious fail
        if len(s) != len(pattern):
            return False

                            # Set up a hashtasble for each letter of the alphabet
        alphahash = []
        for i in range (26):
            alphahash.append(None)

                            # Assign each word to its slot if that slot is empty; if not, it has to match or it's a fail
        for j in range(len(s)):
                            # (-97) is just taking the ASCII for each char and assigning it a 0-25 slot
            index = ord(pattern[j]) - 97

            if alphahash[index] == None:
                alphahash[index] = s[j]
            else:
                if alphahash[index] != s[j] or s[j] != alphahash[index]:
                    return False

                            # If a word ends up assigned to two slots, that's a fail
            if alphahash.count(s[j]) > 1:
                return False

        return True


if __name__ == "__main__":
    print(Solution.wordPattern(Solution,"abbab","dog cat cat dog cat"))