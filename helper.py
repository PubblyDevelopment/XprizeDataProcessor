# helper.py
# Does fun regex stuff
# Initial rename of base64encoded filenames into something readable

import os
import sys
import re
import base64
import json



def makeFilenamesReadable(filepath):
    for root, dirs, files in os.walk(filepath):
        for f in files:
            isJSON = re.search(r"(.*).json", f)

            if (isJSON):
                decodedFilename = base64.b64decode(isJSON.group(1)).decode('utf-8')

                if "/" in decodedFilename:
                    os.rename(os.path.join(root, f), os.path.join(root, decodedFilename.split("/")[0] + decodedFilename.split("/")[-1] + ".json"))
                else:
                    os.rename(os.path.join(root, f), os.path.join(root, decodedFilename + ".json"))
    print ("done.")

def determineIfValidUserAnalyticsFile(filepath):
    rexp = r".{10}-\d-analytics"

    if not filepath.endswith(".json"):
        return False
    if bool(re.search(rexp,filepath)):
        return False
    if os.stat(filepath).st_size is 0:
        return False

    return True

def checkIfValidJson(filepath):
    try:
        with open(filepath, "r") as readFile:
            jsonData = json.load(readFile)
            return jsonData
    except ValueError:
        print("Bad json at", filepath)
        return False
