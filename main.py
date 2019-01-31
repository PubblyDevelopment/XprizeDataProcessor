from helper import *
from dataFile import *
import sys
import json

class dataProcessor:
    def __init__(self, fp, rf):
        self.folderPath = fp
        self.resultFile = rf
        self.allFiles = []

    def play_getAllFiles(self):
        for root, dirs, files in os.walk(self.folderPath):
            for f in files:
                if determineIfValidUserAnalyticsFile(os.path.join(root, f)):
                    j = checkIfValidJson(os.path.join(root, f))
                    if (j):
                        self.allFiles.append(dataFile(root,f,j))
                #iself.allFiles(dataFile(root, f))

    '''def play_writeToCSV(self):
        d = {}
        for f in self.allFiles:
            if f.getIsLesson():
                key = f.getTabId() + "-" + f.getUserId()
                if key in d:
                    d[key] += f.getTimeSpentInFile()
                else:
                    d[key] = f.getTimeSpentInFile()

        f = open(self.resultFile, "w+")
        f.write("userID,totalTime\n")
        for k, v in d.items():
            f.write(k + "," + str(v) + "\n")'''

    def play_writeToCSV(self):
        rFile = open(self.resultFile, "w+")
        rFile.write("subject,time\n")
        d = {}
        for f in self.allFiles:
            key = f.getUserId()
            if key in d:
                d[key] += f.getTimeSpentInFile()
            else:
                d[key] = f.getTimeSpentInFile()

        for k,v in d.items():
            rFile.write(k+","+str(v)+"\n")

    def play_printAllFiles(self):
        for f in self.allFiles:
            print(f)


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
        self.play_writeToCSV()
        #self.play_printAllFiles()

#dp = dataProcessor(sys.argv[1], sys.argv[2])
#dp.main()
print("hello")