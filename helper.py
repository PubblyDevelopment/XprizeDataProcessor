# helper.py
# Does fun regex stuff
# Initial rename of base64encoded filenames into something readable

import os
import sys
import re
import base64
import json
import hashlib
from datetime import datetime as dt
from datetime import *
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

def genAllTimes(filepath):
    new = open(filepath, "a+")

    from datetime import date, timedelta

    d1 = date(2018, 5, 15)  # start date
    d2 = date(2019, 3, 8)  # end date

    delta = d2 - d1         # timedelta

    for i in range(delta.days + 1):
        new.write("0," + str(d1 + timedelta(i)) + ",0.0\n")

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

def getTimeSpentInFile(filepath):
        timestamps = []

        try:
            with open(filepath) as jsonFile:
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

def getFileModifiedDate(filepath):
   return dt.fromtimestamp(os.path.getmtime(filepath))

def getTabID(filename):
    rexp = r"(.{10})-(\d)-(.*)analytics"

    try:
        x = re.search(rexp, filename)
        return x.group(1)
    except:
        print ("Unable to parse filename: ", filename)

def getLessonLevel(filename):
    rexp = r"Hatua%20(\d)"

    try:
        x = re.search(rexp, filename)
        return x.group(1)
    except:
        print ("Unable to parse filename: ", filename)

def getCategory(filename):
    category = ""
    categories = {  "hatua":"lesson",
                    "tutorial":"tutorial",
                    "game": "game",
                    "book":"book",
                    "shelf":"book",
                    "video":"video"}

    for k,v in categories.items():
        if k in filename.lower() and len(category) < 4:
            category += v
            if category == "lesson":
                category += getLessonLevel(filename)
    return category

def mainCSV(filepath):
    v = [0, 240, 240, 243, 247, 244, 235, 241, 244, 248, 146, 242, 237, 243, 247,
            240, 241, 241, 243, 234, 231, 215, 206, 248, 215, 277, 243, 228, 244]
    
    newFile = open("RESULTS_extended.csv","a+")
    newFile.write("village,tabID,days,filename,modified,filesize,category,time\n")
    
    for i in range(1, 29, 1):
        print ("Village:", i)
        for root, dirs, files in os.walk(os.path.join(filepath, str(i))):
            for f in files:
                if determineIfValidUserAnalyticsFile(os.path.join(root, f)) and checkIfValidJson(os.path.join(root, f)):

                    #print(f)
                    vill = i
                    tabID = getTabID(f)
                    days = v[i]
                    mod = getFileModifiedDate(os.path.join(root, f))
                    size = getFileSize(os.path.join(root, f))
                    cat = getCategory(f)
                    time = getTimeSpentInFile(os.path.join(root, f))

                    toCSV = (str(vill) + "," +
                             str(tabID) + "," +
                             str(days) + "," +
                             f[:-5] + "," +
                             str(mod) + "," +
                             str(size) + "," +
                             cat + "," +   
                             str(time) + "\n")

                    #print(toCSV)
                    newFile.write(toCSV)
                    
    
def cleanTimestamps(oldfile, newfile):
    rexp = r"201(8|9)-\d{2}-\d{2}( .+?),"
    
    newFile = open(newfile, "a+")
    oldFile = open(oldfile, "r")

    for line in oldFile:
        try:
            x = re.search(rexp, line)
            newFile.write(line.replace(x.group(2),""))
        except:
            print ("Parse failed @ ", line)
        
def sortDates(filepath):
    dates = []
    dateFile = open(filepath, "r")
    for d in dateFile:
        # Extremely lazy way to strip newlines LOL 
        dates.append(d[0:10])

    return sorted(dates, key=sortHelper)

def sortHelperOld(elem):
    split = elem.split('-')
    return split[0], split[1], split[2]

def genTimeUsage(masterfile, newfile, sorteddates):
    dates = {}
    for d in sorteddates:
        dates[d] = [0, 0]
    
    master = open(masterfile, "r")

    next(master)
    for line in master:
        split = line.split(",")
        dates[split[4]][0] += 1 
        dates[split[4]][1] += float(split[7])

    newFile = open(newfile, "a+")

    newFile.write("date,files,time,avg\n")
    for k,v in dates.items():
        newFile.write(k + "," + str(v[0]) + "," + str(v[1]) + "," + str(v[1]/v[0])+ "\n")

def sortMaster(oldfile, newfile):
    # Get contents of file pre-sort
    wholeFile = []
    master = open(oldfile, "r")
    new = open(newfile, "a+")

    # Skips first line which has the header names, saves column names for later
    columnNames = next(master)
    for line in master:
        wholeFile.append(line)

    sortFile = sorted(wholeFile, key=sortHelper)
    sortFile.insert(0, columnNames)

    for s in sortFile:
        new.write(s)

def sortHelper(elem):
    column = elem.split(",")[4]
    split = column.split("-")
    return split[0], split[1], split[2]

def reduceBySumming(oldfile, newfile):
    master = open(oldfile, "r")
    new = open(newfile, "a+")
    d = {}

    next(master)
    for line in master:
        split = line.split(",")
        if split[4] not in d:
            d[split[4]] = [0.0] * 28
        else:
            # Ridiculous
            d[split[4]][int(split[0])-1] += split[7]
            #d[split[4]][int(split[0])-1] += min(float(split[7]), 0.2698 + 0.0003281 * (float(split[5])))

            #d[split[4]][int(split[0])-1] += 1

    for k,v in d.items():
        for i in range(0, len(v)):
            if v[i] > 0.0:
                new.write(str(i+1) + "," + k + "," + str(v[i]) + "\n")

def getAllTimeStamps(filepath):
    with open(filepath, "r") as readFile:
        jsonData = json.load(readFile)

        timestamps = []
        for j in jsonData:
            timestamps.append(j)

    for t in timestamps:
        print(dt.fromtimestamp(int(t)/1000), "|", t)

def generateAveragesOverTime(oldfile, newfile, date1, date2):
    old = open(oldfile, "r")
    new = open(newfile, "a+")
    dumps = {}

    for i in range(1, 29):
        dumps[i] = []

    
    next(old)
    for line in old:
        split = line.split(',')

        # Using list comp to very LAZILY remove newlines because I'm LAZY
        village, date, time = split[0], split[1], split[2][0:-1]

        dumps[int(village)].append([date, time])

    for k, v in dumps.items():
        village = k
        for i in range(1, len(v)):
            time = v[i][1]
            d1 = v[i-1][0]
            d2 = v[i][0]
            daysBetween = getTimeBetweenTwoDates(d1, d2)
            length = len(daysBetween)
            avg = float(time)/length
            for d in daysBetween:
                new.write(str(village) + "," + d + "," + str(avg) + "\n")



def getTimeBetweenTwoDates(date1, date2):
    '''d1, d2 = [None] * 3, [None] * 3
    
    d1[0], d1[1], d1[2] = int(date1[0:4]),int(date1[5:7]),int(date1[8:10])
    d2[0], d2[1], d2[2] = int(date2[0:4]),int(date2[5:7]),int(date2[8:10])

    x = date(d1[0], d1[1], d1[2])
    y = date(d2[0], d2[1], d2[2])'''

    x = dt.strptime(date1, '%Y-%m-%d')
    y = dt.strptime(date2, '%Y-%m-%d')

    delta = y - x
    
    results = []
    for i in range(abs(delta.days)):
        results.append((x + timedelta(i)).strftime('%Y-%m-%d'))
    return results

def getUniqueTabletsPerDump(filepath):
    d = {}
    data = open(filepath, "r")
    next(data)

    '''for line in data:
        split = line.split(",")
        date, village, tabID = split[4], split[0], split[1]
        print (date, village, tabID, "\n")
        if date in d:
            d[date][int(village)-1].add(tabID)
        else:
            d[date] = [set()] * 28

    for k,v in d.items():
        print (k, v)'''
    for line in data:
        split = line.split(",")
        date, village, tabID = split[4], split[0], split[1]
        if date not in d:
            d[date] = []
            for i in range(0, 28):
                d[date].append([])
        else:
            d[date][int(village)-1].append(tabID)


    '''d["2019-03-08"][4].append("fart")
    for i in d["2019-03-08"]:
        print(i)'''

    for k, v in d.items():
        print ("DATE", k)
        for i in v:
            print (len(set(i)))

    return d

    
#getUniqueTabletsPerDump("RESULTS_sorted.csv")
#getAllTimeStamps("/Users/wallis/Downloads/all data/23/REMOTE/test.json")
#reduceBySumming("RESULTS_sorted.csv","RESULTS_sortedsumreduced.csv")
#genAllTimes("all_times.csv")

#print(getTimeBetweenTwoDates("2018-07-09","2018-07-05"))

generateAveragesOverTime("RESULTS_sortedsum.csv", "RESULTS_normalized.csv")
'''for d in getTimeBetweenTwoDates("2019-04-01","2020-04-01"):
    print (d)'''

#sortMaster("RESULTS_nooutliers.csv", "RESULTS_sorted.csv")
#cleanTimestamps("RESULTS_extended.csv","RESULTS_notimes.csv")
#d = sortDates("/Users/wallis/PycharmProjects/XprizeDataProcessor/uniquedates.txt")
#genTimeUsage("/Users/wallis/PycharmProjects/XprizeDataProcessor/RESULTS_notimes.csv","RESULTS_overtime.csv",d)
#mainCSV(r'C:\Users\Administrator\Desktop\all data')
#makeFilenamesReadable(r'/c/Users/Administrator/Desktop')
#print(getFileModifiedDate(r"C:\Users\Administrator\Desktop\all data\8\REMOTE\5A23002184-2-Hatua%201-Game%203%20dif%201-analytics-947332271020.json"))
#print(getCategory(r"5A23002184-2-Hatua%201-Game%203%20dif%201-analytics-947332271020.json"))
#print(os.path.join(r'C:\Users\Administrator\Desktop\all data', str(5)))