#This is my canvas, this is my art.

"""
Name:                         Benedict&Pack: Find File Listing System (FFLS)
Version:                      1.0
Author:                       Nirman Dave
Description:                  FFLS is a part of the Benedict&Pack which is an artificial intelligence system 
                              that conducts basic functions. The package allows anyone to replicate this system,
                              using few lines of code and embed into apps.
                              FFLS is a simple file search and listing system, that pops up when the user defines 
                              file search.
Publisher:                    SourceNet
Publisher's website:          www.sourcenet.in

Copyright notice, terms & conditions:
(c) Copyrights 2014 by Nirman Dave. All rights reserved.
This work may be modified, reproduced, distributed, performed, and displayed for any purpose
but must acknowledge "Nirman Dave", "SourceNet", "Benedict&Pack" and "Benedict&Pack: FFLS". 
Copyright is retained and must be preserved. The work is provided as is; no warranty is provided,
and users accept all the liability.
"""

#importing modules
import os
from os.path import join

#opening predefined and prewritten files
findfile=open('D:/Softwares/Nirman\'s Python/Benedict/Benedict/FILES/findfile.txt', 'r')
listme=findfile.readlines()
findfile.close()

#conducting the search operation
lookfor = str(listme[0][:-1])
for root, dirs, files in os.walk(str(str(listme[1])+':\\')):
    #listing the search locations
    print "Searching file in: ", root
    if lookfor in files:
        #listing the search result
        print "found: %s" % join(root, lookfor)
        break
