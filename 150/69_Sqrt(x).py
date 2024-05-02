class Solution(object):
    def mySqrt(self, x):
        low = 0
        high = x
        ans = 0

                          # Binary search
        while low <= high:
            mid = (low+high) // 2
            if mid ** 2 > x:
                high = mid - 1
            else:
                ans = mid
                low = mid + 1

        return ans

if __name__ == "__main__":
    print(Solution.mySqrt(Solution,16))