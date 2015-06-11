#!/usr/bin/env python

import sys
import os.path

# This is a tiny script to help you creating a CSV file from yale
#
#  philipp@mango:~/facerec/data/at$ tree
#  .
#  |-- README
#  |-- s1
#  |   |-- 1.pgm
#  |   |-- ...
#  |   |-- 10.pgm
#  |-- s2
#  |   |-- 1.pgm
#  |   |-- ...
#  |   |-- 10.pgm
#  ...
#  |-- s40
#  |   |-- 1.pgm
#  |   |-- ...
#  |   |-- 10.pgm
#

if __name__ == "__main__":

    if len(sys.argv) != 3:
        print "usage: create_csv <base_path> <mode = 0 for training set generation, 1 for test set>"
        sys.exit(1)

    BASE_PATH=sys.argv[1]
    MODE = int(sys.argv[2])
    SEPARATOR=";"

    label = 0
    for dirname, dirnames, filenames in os.walk(BASE_PATH):
        for subdirname in dirnames:
            subject_path = os.path.join(dirname, subdirname)
            cnt = -1.0
            filesindir = len(os.listdir(subject_path))
            for filename in os.listdir(subject_path):
                # For training mode, exit on reaching 80%
                cnt = cnt + 1.0
                if (MODE is 0) and (cnt > (0.8*filesindir)):
                  break
                if ((MODE is 1) and (cnt <= (0.9*filesindir))) :
                  continue
                name1, ext1 = os.path.splitext(filename)
                if( (ext1 != ".pgm") and (ext1 != ".jpg")):
                  break
                if(name1.find("Ambient") != -1):
                  break
                abs_path = "%s/%s" % (subject_path, filename)
                print "%s%s%d" % (abs_path, SEPARATOR, label)
            label = label + 1


