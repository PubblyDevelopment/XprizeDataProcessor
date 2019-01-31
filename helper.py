# helper.py
# Does fun regex stuff
# Initial rename of base64encoded filenames into something readable

import os
import sys
import re
import base64
import json



def makeFilenamesReadable(filepath) :
    #d = base64.b64decode(x.group(1))
    for root, dirs, files in os.walk(filepath):
        for f in files:
            isJSON = re.search(r"(.*).json", f)

            if (isJSON):

                decodedFilename = base64.b64decode(isJSON.group(1)).decode('utf-8')
                print(decodedFilename)
                '''

                if not r"/android_asset/www/" in decodedFilename:
                    print(decodedFilename)
                else:
                    x = re.search(r"android_asset/www/school/tutorials/(.*)-analytics", decodedFilename)
                    y = re.search(r"/android_asset/www/school/Books/.*/(.*)-analytics", decodedFilename)
                    z = re.search(r"/android_asset/www/school/Epic%20Quest/(.*)-analytics", decodedFilename)
                    if (x):
                        print ("EQ-tutorial-" + x.group(1))
                    if (y):
                        print ("EQ-book-" + y.group(1))
                    if (z):
                        print ("EQ-village-" + z.group(1))'''


                '''if not r"/android_asset/www/" in isJSON.group(0):
                    print(isJ)'''

                r"/android_asset/www/school/tutorials/(.*)/"

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

makeFilenamesReadable(r"C:\Users\murac\Documents\XprizeDataProcessing\2019-01-11")
