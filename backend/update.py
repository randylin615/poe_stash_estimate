import requests
import json

### https://poe.ninja/api/data/currencyoverview?league=Settlers&type=Currency
### https://poe.ninja/api/data/itemoverview?league=Settlers&type=KalguuranRune


def get_curr():
    curr = json.loads(
        requests.get(
            "https://poe.ninja/api/data/currencyoverview?league=Settlers&type=Currency"
        ).text
    )
    # print(type(curr))  dict
    curr = curr["lines"]
    # print(type(curr))  dict
    output = []
    for i in curr:
        temp = [
            i["currencyTypeName"],
            1 / i["pay"]["value"] if "pay" in i and "value" in i["pay"] else 0.0,
            i["receive"]["value"] if "receive" in i and "value" in i["receive"] else 0.0,
        ]
        output.append(temp)
    return output


def get_rune():
    rune = json.loads(
        requests.get(
            "https://poe.ninja/api/data/itemoverview?league=Settlers&type=KalguuranRune"
        ).text
    )
    # print(type(rune))  dict
    rune = rune["lines"]
    # print(type(rune))  list
    output = []
    for i in rune:
        temp = [i["name"], i["chaosValue"]]
        output.append(temp)
    # print(type(output[0][0]), type(output[0][1]))) str, float
    return output
