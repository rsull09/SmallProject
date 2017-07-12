
import re

rawdata = open(r"C:\Input_Filepath.txt", 'r')
finaldata = open(r"C:\Output_Filepath.txt", 'w')

for line in rawdata:
    if re.match("208.5\s",line):
        print >> finaldata, line,
rawdata.close()
finaldata.close()

print 'Done.'
