import json

def alternative_parser(message:str) -> dict:
    replaced = message.replace("None","null")
    parsed = json.loads(replaced)

    return parsed