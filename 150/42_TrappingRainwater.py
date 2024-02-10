class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """

        layers = max(height)

        water_total = 0

                                # Make each layer into 1s and 0s
        while layers > 0:
                                # an empty layer, first
            current_layer = []
            for h in height:
                current_layer.append(0)

            for m in range(len(height)):
                if height[m] >= layers:
                    current_layer[m] = 0
                else:
                    current_layer[m] = 1   

                                # Remove 1s at start and end
            while current_layer[0] == 1:
                del current_layer[0]
            while current_layer[len(current_layer)-1] == 1:
                del current_layer[-1]

                                # Count the trapped water, add it to the total
            water_total += sum(current_layer)

            layers -= 1

        return water_total


if __name__ == "__main__":
    print(Solution.trap(Solution,[2,67,4,57,23,3,6,67,5,3,2,4,6,7,43,9]))