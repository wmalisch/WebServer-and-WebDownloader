import re
import os


filePath = "/foo.txt"
if(filePath[0] =='/'):
    filePath = '.' + filePath
    newFile = filePath[1:len(filePath)-1]
if(filePath[0] != '.' and filePath[1] != '/'):
    filePath = './' + filePath
    newFile = filePath
if(filePath[0] == '.' and filePath[1] == '/'):
    newFile = filePath[2:len(filePath)-1]
else:
    newFile = filePath


print(filePath)
print(newFile)