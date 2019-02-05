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
                try:
                    decodedFilename = base64.b64decode(isJSON.group(1)).decode('utf-8')

                    if "/" in decodedFilename:
                        os.rename(os.path.join(root, f), os.path.join(root, decodedFilename.split("/")[0] +
                                                                      decodedFilename.split("/")[-1] + ".json"))
                    else:
                        os.rename(os.path.join(root, f), os.path.join(root, decodedFilename + ".json"))
                except:
                    print ("Decode failed at", f)


    print ("done.")

def determineIfValidUserAnalyticsFile(filepath):
    rexp = r".{10}-\d-analytics"

    if not filepath.endswith(".json"):
        return False
    if not "analytics" in filepath:
        return False
    if (re.search(rexp,filepath)):
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
    foundFilenames = []

    for d in dates:
        print("DATE:", d)
        for root, dirs, files in os.walk(os.path.join(filepath, d)):
            for f in files:
                print(f)
                if f in foundFilenames:
                    os.remove(os.path.join(root,f))
                else:
                    foundFilenames.append(f)



    print (foundFilenames)

def syllTapTester():
    x = 91 - 50
    y = 83 - 61
    ## Expected output: 35

    # Make grid:
    counter = 1
    grid = []
    for i in range(0,10):
        grid.append([])
        for j in range(0,10):
            grid[i].append(counter)
            counter += 1

    for i in range(0,10):
        for j in range(0,10):
            print (grid[i][j], end=" ")
        print("\n")

    cdX = int((x-(x%90)) / 90)
    cdY = int((y-(y%56)) / 56) - 1
    print( grid[cdY][cdX]  )
#makeFilenamesReadable("/Users/wallis/Dev/XprizeDataProcessing/BOXDATA/2019-01-25")
#print(base64.b64decode("NjExMjAwMDEyMS0yLS9hbmRyb2lkX2Fzc2V0L3d3dy9zY2hvb2wvRXBpYyUyMFF1ZXN0L3ZhcmlhYmxlLUVRX0cyX1BvdHRlcnktRVFfRzJfUG90dGVyeS5odG1sLWFuYWx5dGljcy0xNTQ3Mzk1NDYxMDY0").decode('utf-8'))
syllTapTester()