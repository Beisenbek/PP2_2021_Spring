import re
a = "1,2;3#4,5"

for x in (re.split(',|;|#',a)):
    print(x)