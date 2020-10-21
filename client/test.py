import re
import os

text = 'GET ./client.py HTTP1.1'

m = re.search(' (.+?) ', text)
if m:
    found = m.group(1)

bar = os.path.isfile(found)
print(bar)
print(found)
print(len(found))