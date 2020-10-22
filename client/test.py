import re
import os


filePath = "/foo.txt"
if(filePath[0] =='/'):
    filePath = '.' + filePath
    newFile = filePath[1:len(filePath)]
if(filePath[0] != '.' and filePath[1] != '/'):
    filePath = './' + filePath
    newFile = filePath
if(filePath[0] == '.' and filePath[1] == '/'):
    newFile = filePath[2:len(filePath)]
else:
    newFile = filePath


print(filePath)
print(newFile)

with open(newFile,"w") as f:
    f.write("Lets test out this assignment and get the thing submitted")