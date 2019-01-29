from helper import *
from dataFile import *
import sys
import json

class dataProcessor:
    def __init__(self, folderPath):
        self.filepath = folderPath
        self.allFiles = []

    def play_getAllFiles(self):
        for root, dirs, files in os.walk(self.filepath):
            for f in files:
                self.allFiles.append(dataFile(root,f))
                #iself.allFiles(dataFile(root, f))

    ''' ### REWRITE THIS it's bad ###
    def play_getTimeSpentInEachNode(self):
        self.times = []
        for f in self.allFiles:
            if f.determineIfValidUserAnalyticsFile():
                try:
                    self.times.append(f.determineTimeSpentInNode())
                except:
                    print("Failed at:",f.getFilepath())

    def play_getAverageTimeSpentInDay(self):
        totalSum = 0
        for t in self.times:
            totalSum += t

        print(totalSum/7)
    '''

    def main(self):
        self.play_getAllFiles()
        self.play_getTimeSpentInEachNode()
        self.play_getAverageTimeSpentInDay()

dp = dataProcessor(sys.argv[1])
dp.main()