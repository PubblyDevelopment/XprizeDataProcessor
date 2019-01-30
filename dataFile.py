# dataFile.py
# Represents a data file, can store useful info about the file?
# Maybe worth having it write to a CSV........?

import json
import os
import re

class dataFile:
    def __init__(self, root, fname, j):
        self.filepath = os.path.join(root, fname)
        self.filename = fname
        self.jsonData = j
        self.parseFilename()

    def __str__(self):
        toPrint = self.subject[0].capitalize() + ": " + self.tabId + "-" + self.userId + ": " + self.title

        return toPrint

    def getFilepath(self):
        return self.filepath

    def getFilename(self):
        return self.filename

    def getTabId(self):
        return self.tabId

    def getSubject(self):
        return self.subject

    def getUserId(self):
        return self.userId

    def parseFilename(self):
        rexp = r"^(.{10})-(\d)-(.*)-analytics-\d{12}"

        try:
            x = re.search(rexp, self.filename)
            self.tabId = x.group(1)
            self.userId = x.group(2)
            self.title = x.group(3)
        except:
            print ("Unable to parse filename")

        if "tutorials" in self.filename:
            self.subject = "tutorial"
        elif "Game" in self.filename:
            self.subject = "game"
        elif "Lesson" in self.filename:
            self.subject = "lesson"
        else:
            self.subject = "book"

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

        return (float(timestamps[-1])-float(timestamps[0]))/60000

d = dataFile("fartFolder/", "5A27001608-2-Hatua%202-Lesson%20A-analytics-947265221619.json", "jsondata")