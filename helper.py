# helper.py
# Does fun regex stuff
# Initial rename of base64encoded filenames into something readable

import os
import sys
import re
import base64
import json
import hashlib

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

def hash_file(filename):
    h = hashlib.md5()

    with open(filename, 'rb') as file:
        chunk = 0
        while chunk != b'':
            chunk = file.read(1024)
            h.update(chunk)

    return h.hexdigest()

def duplicateRemover(filepath):
    dates = next(os.walk(filepath))[1]
    foundHashes = []

    for d in dates:
        print("DATE:", d)
        for root, dirs, files in os.walk(os.path.join(filepath, d)):
            for f in files:
                h = hash_file(os.path.join(root,f))
                if h in foundHashes:
                    print("File removed")
                    os.remove(os.path.join(root,f))
                else:
                    foundHashes.append(h)



    print (foundHashes)

duplicateRemover("/Users/wallis/Dev/XprizeDataProcessing/BOXDATA")