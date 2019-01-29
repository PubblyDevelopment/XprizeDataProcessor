# dataFile.py
# Represents a data file, can store useful info about the file?
# Maybe worth having it write to a CSV........?

import json

class dataFile:
    def __init__(self, filepath):
        self.fileLoc = filepath

    def getFilepath(self):
        return self.fileLoc

    def determineTimeSpentInNode(self):
        with open(self.fileLoc, "r") as readFile:
            jsonData = json.load(readFile)

            ## Make time stamps into list, then get first to last
            ## Could sort to be certain? But should theoretically not be out of order
            ## (Would indicate larger problem????)
            timestamps = []
            for j in jsonData:
                timestamps.append(j)

            timeInNode = (float(timestamps[-1])-float(timestamps[0]))/60000.0

            # Should be 947871176576 and 947871438462
            print("Time in lesson" , timeInNode, "minutes")