
class Solution(object):
    def fullJustify(self,words,maxwidth):

        output = ""

        line_arr = []
        line = ""

                            # Set and remove zeroth word in array of words, til array is empty
        #while words:


                            # takes an ARRAY of words as a single line, adds spaces til it
    def padLine(self,line,maxwidth):
        width = sum(len(word) for word in line)

        cycle = len(line)-1
        caret = 0

        for i in range (maxwidth-width):
            line[caret % cycle] += " "
            caret += 1

        line = str(line)

        return line




if __name__ == "__main__":
    #print(Solution.fullJustify(Solution, ["Science","is","what","we","understand","well","enough","to","explain","to","a","computer.","Art","is","everything","else","we","do."],16))
    #print(Solution.fullJustify(Solution, ["Fox."],16))

    print(Solution.padLine(Solution,["Science","is","what","we"],16))