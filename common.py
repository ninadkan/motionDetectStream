from pathlib import Path
import json

def is_json(myjson):
    json_object = None
    try:
        json_object = json.loads(myjson)
    except Exception as e:
        #print("Not json")
        return False, json_object
    return True, json_object

