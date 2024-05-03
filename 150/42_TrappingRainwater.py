class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """

        layers = max(height)
        pillars = len(height)

        water_total = 0

        last_two = [0,0]
        water = False


        for i in range(layers,0,-1):
                            # Stack for storing water as it is counted
            water_layer = []

            for j in range(pillars-1):
                last_two[0] = last_two[1]
                water = False
                if height[j] >= i:
                    last_two[1] = 1
                else:
                    last_two[1] = 0

                if last_two == [0,1] and water == True:
                    water == False

                if last_two == [1,0]:
                    water = True
                    water_layer.insert(0,1)

                if last_two == [0,0] and water == True:
                    water_layer[0] += 1

                if j == pillars and last_two == [0,0] and water == True:
                    water = False
                    del water_layer[0]

                print(last_two)

            print(water_layer)


        return water_total


if __name__ == "__main__":
    print(Solution.trap(Solution,[2,0,0,0,1,0])) #[2,67,4,57,23,3,6,67,5,3,2,4,6,7,43,9]))