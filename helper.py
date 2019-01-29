# helper.py
# Does fun regex stuff
# Initial rename of base64encoded filenames into something readable

import os
import sys
import re
import base64

def makeFilenamesReadable(filepath) :
    rexp = "(.*).json"

    ### Walk thru all files, print out decoded base64 filename w/out
    ### little b thing (convert ascii to string essentially)
    for root, dirs, files in os.walk(filepath):
        for f in files:
            x = re.search(rexp, f)
            if (x):
                d = base64.b64decode(x.group(1))

                os.rename(os.path.join(root, f), os.path.join(root,d.decode('ascii')+".json"))
    print ("done.")

