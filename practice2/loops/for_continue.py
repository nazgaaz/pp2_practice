
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    if x == "banana":
        continue
    print(x)



for i in range(10):
    if i % 2 == 0:
        continue
    print(i)



text = "a b  c"
for ch in text:
    if ch == " ":
        continue
    print(ch)


words = ["hi", "hello", "ok", "python"]
for w in words:
    if len(w) < 3:
        continue
    print(w)


for i in range(1, 8):
    if i == 4:
        continue
    print(i)
