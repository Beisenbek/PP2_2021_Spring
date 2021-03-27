f = open("input.txt", "r")
l = f.readlines()

n = int(input())
for x in range(n):
  print(l[n - x])