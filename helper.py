# helper.py
# Does fun regex stuff
# Initial rename of base64encoded filenames into something readable

import os
import sys
import re
import base64
import json



def makeFilenamesReadable(filepath) :
    rexp = r"(.*).json"

    fp = "NjExMjAwMTIwNS0xLS9hbmRyb2lkX2Fzc2V0L3d3dy9zY2hvb2wvRXBpYyUyMFF1ZXN0L3ZhcmlhYmxlLUVRX1NhbXBsZXItRVFfU2FtcGxlci5odG1sLWFuYWx5dGljcy0xNTQ2NjgzNzI1ODc0.json"

    x = re.search(rexp, fp)

    print(x.group(1))

    d = base64.b64decode(x.group(1))

    print(d)

    '''errorcount = 0
    ### Walk thru all files, print out decoded base64 filename w/out
    ### little b thing (convert ascii to string essentially)
    for root, dirs, files in os.walk(filepath):
        for f in files:
            x = re.search(rexp, f)
            if (x):
                try:
                    d = base64.b64decode(x.group(1))
                    errorcount += 1
                except:
                    print ("Failed at",filepath)

                #os.rename(os.path.join(root, f), os.path.join(root,d.decode('ascii')+".json"))'
                print(d)

    print("Errors",errorcount)'''



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

makeFilenamesReadable("/Users/wallis/Dev/XprizeDataProcessing/BOXDATA/2019-01-11")