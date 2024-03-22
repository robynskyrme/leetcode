# class Solution(object):
    # def fullJustify(self, words, maxWidth):
    #     """
    #     :type words: List[str]
    #     :type maxWidth: int
    #     :rtype: List[str]
    #     """
    #
    #     justifiedText = []
    #
    #     while words:
    #         print(words)
    #         currentLine = 1
    #
    #
    #         while Solution.getLength(self,words,currentLine) < maxWidth:
    #             currentLine += 1
    #
    #         currentLine -= 2
    #
    #
    #         words[currentLine] = Solution.removeTrailingSpaces(self,words[currentLine])
    #
    #         addspaces = 0
    #         while Solution.getLength(self,words,currentLine) < maxWidth:
    #             words[addspaces % currentLine] += " "
    #             addspaces += 1
    #
    #         line = ""
    #         for concat in range(currentLine+1):
    #             line += words[concat]
    #         justifiedText.append(line)
    #
    #         for each in justifiedText:
    #             print(each + "\n")
    #         # print(justifiedText)
    #
    #         for remove in range(currentLine+1):
    #             del words[0]
    #
    #         print(words)
    #
    #
    #
    # def getLength(self,array,count):
    #     length = 0
    #     for word in range(count):
    #         length += len(array[word])
    #     #print(length)
    #     return length+(count-1)
    # def removeTrailingSpaces(self,word):
    #     while word[-1] == " ":
    #         word = word[:-1]
    #     return word






                            # Another approach, which also doesn't work

                            # (This one is annoying me, a lot)

class Solution(object):
    def fullJustify(self, words, maxwidth):
        justifiedText = ""

        lines = [[0]]
        line = 0

                            # Place words in a line until no more will fit;
                            # then move onto the next line
        while words:
            newlen = len(words[0])
            if lines[line][0] + newlen < maxwidth:
                lines[line].append(words[0])
                lines[line][0] += newlen
                lines[line][len(lines[line])-1] += " "
                del words[0]
            else:
                lines.append([0])
                line += 1
                lines[line].append(words[0])
                lines[line][0] += newlen
                del words[0]

                            # (Catch the last one)

                            # Make the output by repeatedly adding extra spaces to all but the last word, cycling L-R
                            # (applies to all but the last line)
        print(lines)

        line = 0
        while len(lines) > 0:
            width = lines[line][0]
            del lines[line][0]
            count = 0
            while width < maxwidth:
                cycle = len(lines[line]) - 1
                if cycle == 0:
                    cycle = 1
                lines[line][count % cycle] += " "
                count += 1
                width += 1

            for each in lines[line]:
                justifiedText += each
            justifiedText += "\n"
            del lines[line]





        print(lines)


        return justifiedText


if __name__ == "__main__":
    print(Solution.fullJustify(Solution, ["Science","is","what","we","understand","well","enough","to","explain","to","a","computer.","Art","is","everything","else","we","do."],16))