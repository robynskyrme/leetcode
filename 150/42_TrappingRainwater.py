def trap(height):
    """
    :type height: List[int]
    :rtype: int
    """

    layers = max(height)
    current_layer = []
    for h in height:
        current_layer.append(0)

    while layers > 0:
        for m in range(len(height)):
            print(height[m])
            if height[m] >= layers:
                current_layer[m] = 1
            else:
                current_layer[m] = 0
        print(current_layer)
        layers -= 1

    return 1



if __name__ == "__main__":
    trap([0,1,0,2,1,0,1,3,2,1,2,1])