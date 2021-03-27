x = int(input())
patternNext = "The next number for the number {} is {}."
patternPrev = "The previous number for the number {} is {}."
print(patternNext.format(x, x + 1))
print(patternPrev.format(x, x - 1))