import json

def loadData(inputFile: str):
    jsonData = json.load(open('input.json'))
    assert jsonData["factory_rod_size"] > 0, "Rod size cannot be smaller than 1"

    for i in jsonData["order"]:
        assert i["rod_size"] <= jsonData["factory_rod_size"], "Required rod size cannot exceed lenght of rod produced by factory"
        assert i["rods_number"] > 0, "Number of rods cannot be smaller than 1"
        assert i["relaxation_number"] >= 0, "Number of rods cannot be smaller than 0"
        assert i["relaxation_length"] >= 0, "Relaxation amount cannot be smaller than 0"
        assert i["relaxation_number"] <= i["rods_number"], "Number of rods cannot be smaller than number of rods that can be relaxed!"
    return jsonData

def getOrderLengths(jsonFile):
    lengths = []
    for i in jsonFile["order"]:
        lengths.append([i["rods_number"], i["rod_size"]])

    return lengths

def expandOrder(input):
    lengths = []
    for i in range(len(input)):
        for j in range(input[i][0]):
            lengths.append(input[i][1])

    return lengths


def getRelaxedOrderLengths(jsonFile):
    lengths = []
    for i in jsonFile["order"]:
        for j in range(i["relaxation_number"]):
            lengths.append(i["rod_size"] - i["relaxation_length"])
        for j in range(i["rods_number"] - i["relaxation_number"]):
            lengths.append(i["rod_size"])
    return lengths