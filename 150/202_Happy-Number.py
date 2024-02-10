class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """

        digits = self.digitsArray(self,n)

        visited = []

        sum = 0

        while n > 1:
            if visited.count(n) > 1:
                return False

            sum = 0

            digits = self.digitsArray(self, n)

            for each in digits:
                sum += each ** 2

            visited.append(sum)
            n = sum

        return True



    def digitsArray(self,n):
        digits = []

        while n:
            digits.insert(0,n % 10)
            n = n//10

        return digits


if __name__ == "__main__":
    print(Solution.isHappy(Solution,100))