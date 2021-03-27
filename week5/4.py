thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

thisdict2 = {
  "brand": "Ford",
  "model": "Mustang2",
  "year": 1965
}

for i1,i2 in zip(thisdict.items(),thisdict2.items()):
    if(i1 == i2):
        print("same")
    else:
        print("not same")