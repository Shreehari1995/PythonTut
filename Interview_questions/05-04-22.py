# comma separated string

s = "hello welcome to python"

# separating each character
# list_ = list(s)

words = s.split()
print(words)
print(*words, sep=",")
