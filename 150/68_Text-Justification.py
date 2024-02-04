class Solution(object):
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """

        justifiedText = []

        while words:
            print(words)
            currentLine = 1


            while Solution.getLength(self,words,currentLine) < maxWidth:
                currentLine += 1

            currentLine -= 2


            words[currentLine] = Solution.removeTrailingSpaces(self,words[currentLine])

            addspaces = 0
            while Solution.getLength(self,words,currentLine) < maxWidth:
                words[addspaces % currentLine] += " "
                addspaces += 1

            line = ""
            for concat in range(currentLine+1):
                line += words[concat]
            justifiedText.append(line)

            for each in justifiedText:
                print(each + "\n")
            # print(justifiedText)

            for remove in range(currentLine+1):
                del words[0]

            print(words)



    def getLength(self,array,count):
        length = 0
        for word in range(count):
            length += len(array[word])
        #print(length)
        return length+(count-1)
    def removeTrailingSpaces(self,word):
        while word[-1] == " ":
            word = word[:-1]
        return word



if __name__ == "__main__":
    Solution.fullJustify(Solution, ["Science","is","what","we","understand","well","enough","to","explain","to","a","computer.","Art","is","everything","else","we","do"],16)