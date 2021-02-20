import re

file = open('raw.data','r')
text = file.read()

BINPattern = r"\nБИН.*(?P<BIN>\b[0-9]+)"
NDSPattern = r"\nНДС.*(?P<NDS>\b[0-9]+)"

BINText = re.search(BINPattern, text).group("BIN")
NDSText = re.search(NDSPattern, text).group("NDS")

print(NDSText)
print(BINText)

file.close()