
i = 0
while i < 6:
    i += 1
    if i == 3:
        continue
    print(i)


i = 0
while i < 10:
    i += 1
    if i % 2 == 0:
        continue
    print(i)


items = ["hi", "", "bye", ""]
i = 0
while i < len(items):
    if items[i] == "":
        i += 1
        continue
    print(items[i])
    i += 1


i = 0
while i < 10:
    i += 1
    if i < 5:
        continue
    print(">=5:", i)


words = ["cat", "skip", "dog", "bird"]
i = 0
while i < len(words):
    if words[i] == "skip":
        i += 1
        continue
    print(words[i])
    i += 1
