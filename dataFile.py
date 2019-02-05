# dataFile.py
# Represents a data file, can store useful info about the file?
# Maybe worth having it write to a CSV........?

import json
import os
import re

class dataFile:
    def __init__(self, root, fname, j, v, w):
        self.tabId = None
        self.userId = None
        self.title = None
        self.timeSpentInFile = None
        self.category = ""
        self.isEQ = None

        self.filepath = os.path.join(root, fname)
        self.filename = fname
        self.jsonData = j
        self.villageNum = v
        self.weekNum = w
        self.time = self.getTimeSpentInFile()

        self.categories = { "tutorial":"tutorial",
                            "game": "game",
                            "book":"book",
                            "shelf":"book",
                            "hatua":"lesson",
                            "video":"video"}


        self.parseFilename()

    def __str__(self):
        #toPrint = self.subject[0].capitalize() + ": " + self.tabId + "-" + self.userId + ": " + self.title

        return ("== " + self.title + "== \n" +
               "TabletID: " + self.tabId + "\n" +
               "UsrID: " + self.userId + "\n" +
               "UniqueID: " + self.tabId + "-" + self.userId + "\n" +
               "WeekNum: " + self.weekNum + "\n" +
               "Category: " + self.category + "\n" +
               "EpicQuest: " + str(self.isEQ) + "\n" +
               "VillageNum: " + str(self.villageNum) + "\n" +
               "TimeInFile: " + str(self.time) )

    def getFilepath(self):
        return self.filepath

    def getFilename(self):
        return self.filename

    def getTabId(self):
        return self.tabId

    def getUserId(self):
        return self.userId

    def getUniqueId(self):
        return self.tabId + "-" + self.getUserId()

    def getTimeInFile(self):
        return self.time

    def getTitle(self):
        return self.title

    def getCategory(self):
        return self.category

    def getSubject(self):
        return self.subject

    def getIsEQ(self):
        return self.isEQ

    def getVillageNum(self):
        return self.villageNum

    def getWeekNum(self):
        return self.weekNum

    def getFilepath(self):
        return self.filepath

    def parseFilename(self):
        rexp = r"(.{10})-(\d)-(.*)analytics"

        try:
            x = re.search(rexp, self.filename)
            self.tabId = x.group(1)
            self.userId = x.group(2)
            self.title = x.group(3)
        except:
            print ("Unable to parse filename: ", self.filename)

        if "EQ" in self.title:
            self.isEQ = True
            self.category += "EQ-"
        else:
            self.isEQ = False

        for k,v in self.categories.items():
            if k in self.title.lower() and len(self.category) < 4:
                self.category += v

    def determineTimeSpentInNode(self):
        with open(self.filepath, "r") as readFile:
            jsonData = json.load(readFile)

            timestamps = []
            for j in jsonData:
                timestamps.append(j)

            return (float(timestamps[-1]) - float(timestamps[0])) / 60000

    '''' rewrite this garbage too
    def determineTimeSpentInNode(self):
        with open(self.filepath, "r") as readFile:
            jsonData = json.load(readFile)

            ## Make time stamps into list, then get first to last
            ## Could sort to be certain? But should theoretically not be out of order
            ## (Would indicate larger problem????)
            minTimestamp = None
            maxTimestamp = None
            timestamps = []
            for j in jsonData:
                timestamps.append(j)
            #
            #print("Min:", minTimestamp, "Max:", maxTimestamp)

            timeInNode = (float(timestamps[-1])-float(timestamps[0]))/60000

            return timeInNode
    '''
    def getTimeSpentInFile(self):
        timestamps = []

        for j in self.jsonData:
            timestamps.append(j)

        if timestamps[-1].endswith("-1"):
            return (float(timestamps[-2])-float(timestamps[0]))/60000
        else:
            return (float(timestamps[-1])-float(timestamps[0]))/60000

#d = dataFile("fartFolder/", "5A27001608-2-Hatua%202-Lesson%20A-analytics-947265221619.json", "jsondata")

print (bool("1547137654847-1".endswith("-1")))

print ("FART")