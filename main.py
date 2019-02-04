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
        osWalk = os.walk(self.folderPath)
        dates = next(osWalk)[1]
        for root, dirs, files in os.walk(self.folderPath):
            for f in files:
                if determineIfValidUserAnalyticsFile(os.path.join(root, f)):
                    j = checkIfValidJson(os.path.join(root, f))
                    if (j):
                        v = root.split("/")[-2]
                        for d in dates:
                            print(d)
                            if d in os.path.join(root, f):
                                self.allFiles.append(dataFile(root,f,j,v, d))

    def test_getAllFiles(self):
        osWalk = os.walk(self.folderPath)
        dates = next(osWalk)[1]
        for root, dirs, files in os.walk(self.folderPath):
            for f in files:
                for d in dates:
                    if d in os.path.join(root, f):
                        print(f, "-->", d)

    def play_writeToCSV(self):
        rFile = open(self.resultFile, "w+")
        rFile.write("tabID,userID,uniqueID,filename,time,category,EQ,villageNum,weekNum\n")
        for f in self.allFiles:
            if len(f.getCategory()) > 0:
                rFile.write(f.getTabId() + "," +
                        f.getUserId() + "," +
                        f.getUniqueId() + "," +
                        f.getTitle() + "," +
                        str(f.getTimeInFile()) + "," +
                        f.getCategory() + "," +
                        str(f.getIsEQ()) + "," +
                        str(f.getVillageNum()) + "\n" +
                        str(f.getWeekNum())   )

    def play_printAllFiles(self):
        for f in self.allFiles:
            print (f)

        print (self.allFiles)

    def main(self):
        #self.test_getAllFiles()
        self.play_getAllFiles()
        self.play_writeToCSV()
        #self.play_printAllFiles()

dp = dataProcessor(sys.argv[1], sys.argv[2])
dp.main()
