# dataFile.py
# Represents a data file, can store useful info about the file?
# Maybe worth having it write to a CSV........?

import json
import os
import re

class dataFile:
    def __init__(self, root, fname):
        self.filepath = os.path.join(root, fname)
        self.filename = fname
        self.timeInNode = self.determineTimeSpentInNode()

    def getFilepath(self):
        return self.filepath

    def getFilename(self):
        return self.filename

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

    def determineIfValidUserAnalyticsFile(self):
        rexp = r".{10}-\d-analytics"

        if not self.filename.endswith(".json"):
            return False
        if bool(re.search(rexp,self.filename)):
            return False
        if os.stat(self.filepath).st_size is 0:
            return False

        return True