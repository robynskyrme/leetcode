class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """

        layers = max(height)
        pillars = len(height)

        water_total = 0

        water = False


        for i in range(layers,0,-1):
            last_two = [0, 0]
                            # Stack for storing water as it is counted
            water_layer = []

            # No water is collected at the left edge of a layer
            water = False

            for j in range(pillars):
                            # Set the current brick to the previous
                last_two[0] = last_two[1]


                            # Set the current brick (does it exist, or not)
                if height[j] >= i:
                    last_two[1] = 1
                else:
                    last_two[1] = 0

                            # Individual cases for what to do
                            # If there is no brick, and there was none before, do nothing
                            # If there was a brick, and now is nothing, start counting water
                if last_two == [1,0]:
                    water_layer.insert(0,1)
                    water = True

                            # If it's enclosed space, and we're counting water, count that water!
                if last_two == [0,0] and water == True:
                    water_layer[0] += 1

                            # If we hit rock, stop counting water
                if last_two == [0,1]:
                    water = False

                            # If we are still counting water, but we hit the end of a layer... discard that count
                if last_two[1] == 0 and j == pillars-1:
                    del water_layer[0]


                #print(last_two)

            #print("\n")

            water_total = water_total + sum(water_layer)



        return water_total


if __name__ == "__main__":
    print(Solution.trap(Solution,[2,67,4,57,23,3,6,67,5,3,2,4,6,7,43,9]))