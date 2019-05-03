# helper.py
# Does fun regex stuff
# Initial rename of base64encoded filenames into something readable

import os
import sys
import re
import base64
import json
import hashlib
from shutil import copyfile

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

def bad_syllTapTester():
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
    print( grid[cdY][cdX] )

def checkIfAnyFilesUnaccessed(accFile, allFile):
    print("fart")

    with open(accFile) as f:
        accFiles = f.read().splitlines()

    with open(allFile) as g:
        allFiles = g.read().splitlines()

    accFiles.sort()
    allFiles.sort()

    for i in range(0, len(allFiles)):
        if allFiles[i] not in accFiles:
            print (allFiles[i])

def countInteractions(filepath):
    jsons = []
    for root, dirs, files in os.walk(filepath):
        for f in files:
            if f.endswith(".json"):
                try:
                    with open(os.path.join(root, f), "r") as readFile:
                        jsonData = json.load(readFile)
                        jsons.append((os.path.join(root,f), jsonData, f))
                except:
                    print("JSON failed at",f)

    counter = 0
    for j in jsons:
        if len(j[1]) > 20:
            print (j[0])
            copyfile(j[0],os.path.join("/Users/wallis/Dev/XprizeDataProcessing/EQ_Village_Files_Richard",j[2]))
            counter += 1
    print(counter)

def getTimeSpentInFile(filename):
        timestamps = []

        try:
            with open(filename) as jsonFile:
                jsonData = json.load(jsonFile)
                for j in jsonData:
                    timestamps.append(j)

            if timestamps[-1].endswith("-1"):
                return (float(timestamps[-2])-float(timestamps[0]))/60000
            else:
                return (float(timestamps[-1])-float(timestamps[0]))/60000
        except:
            print ("Bad JSON @", filename)

def getFileSize(filename):
    return os.stat(filename).st_size

def mainRead(filepath):
    makeFilenamesReadable(filepath)

def getTabID(filename):
    rexp = r"(.{10})-(\d)-(.*)analytics"

    try:
        x = re.search(rexp, filename)
        return x.group(1)
    except:
        print ("Unable to parse filename: ", filename)

def mainCSV(filepath):
    print ("???")
    v = [0, 240, 240, 243, 247, 244, 235, 241, 244, 248, 146, 242, 237, 243, 247,
            240, 241, 241, 243, 234, 231, 215, 206, 248, 215, 277, 243, 228, 244]
    finalCSV = ""
    
    for i in range(1, 29, 1):
        print ("Village:", i)
        for root, dirs, files in os.walk(os.path.join(filepath, str(i))):
            for f in files:
                if determineIfValidUserAnalyticsFile(os.path.join(root, f)) and checkIfValidJson(os.path.join(root, f)):

                    #print(f)
                    vill = i
                    tabID = getTabID(f)
                    days = v[i]
                    time = getTimeSpentInFile(os.path.join(root, f))
                    
                    finalCSV += str(vill) + "," + tabID + "," + str(days) + "," + str(time) + "\n"
                    



    newFile = open("RESULTS.csv","w+")
    newFile.write(finalCSV)



mainCSV(r'C:\Users\Administrator\Desktop\all data')
#makeFilenamesReadable(r'/c/Users/Administrator/Desktop')
#print(getTabID("6115001102-2-Hatua%201-Lesson%2027-analytics-947126900136.json"))
#print(os.path.join(r'C:\Users\Administrator\Desktop\all data', str(5)))