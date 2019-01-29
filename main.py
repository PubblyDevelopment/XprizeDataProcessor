from helper import *
from dataFile import *
import sys
import json

class dataProcessor:
    def __init__(self, folderPath):
        self.filepath = folderPath

    def play_lookAtAFile(self, fileObject):
        print(fileObject.getFilepath())

        fileObject.determineTimeSpentInNode()

    def main(self):
        print(self.filepath)
        aFile = dataFile(os.path.join(self.filepath, "5/REMOTE/5A29000537-2-Hatua%203-Lesson%202-analytics-948525813472.json"))
        self.play_lookAtAFile(aFile)


dp = dataProcessor(sys.argv[1])
dp.main()