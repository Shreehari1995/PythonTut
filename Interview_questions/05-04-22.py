# comma separated string

s = "hello welcome to python"

# separating each character
# list_ = list(s)

# words = s.split()
# print(words)
# print(*words, sep=",")

###############################################################################################
s = "hello welcome to python"
res = ""
for char in s:
    if s.count(char) > 1:   # if char in res:
        res = res + "-"
    else:
        res = res + char










