import json
import random


def generateData(relaxation=False, max_percentage=50, factory_rod_size=15, order_size=10):
    order = []
    while order_size > 0:
        rod_size = random.randint(1, factory_rod_size - 1)
        rods_number = random.randint(1, order_size)
        order_size -= rods_number
        if order_size < 0:
            rods_number += order_size

        relaxation_length = random.randint(0, max_percentage)
        relaxation_number = random.randint(0, rods_number)
        if not relaxation:
            relaxation_length = 0
            relaxation_number = 0

        order.append({"rod_size": rod_size, "rods_number": rods_number, "relaxation_length": relaxation_length, "relaxation_number": relaxation_number})

    return {"factory_rod_size": factory_rod_size, "order": order}


with open("input.json", "w") as outfile:
    data = generateData()
    json = json.dumps(data)
    outfile.write(json)
