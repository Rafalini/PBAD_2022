import DataLoader

def firstFit(weight, factoryRodSize):
    res = 0
    # Create an array to store remaining space in bins
    bin_rem = [0] * len(weight)
    for i in range(len(weight)):
        # Find the first bin that can accommodate weight[i]
        j = 0
        min = factoryRodSize + 1
        bi = 0

        for j in range(res):
            if (bin_rem[j] >= weight[i] and bin_rem[j] - weight[i] < min):
                bi = j
                min = bin_rem[j] - weight[i]

        # If no bin could accommodate weight[i],
        # create a new bin
        if (min == factoryRodSize + 1):
            bin_rem[res] = factoryRodSize - weight[i]
            res += 1
        else:  # Assign the item to best bin
            bin_rem[bi] -= weight[i]
    return res


if __name__ == '__main__':
    jsonData = DataLoader.loadData("input.json")
    weight = DataLoader.getRelaxedOrderLengths(jsonData)
    weight = DataLoader.expandOrder(weight)
    n = len(weight)
    print("Number of bins required in: " + str(firstFit(weight, jsonData["factory_rod_size"])))
