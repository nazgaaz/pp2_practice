
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)
    if x == "banana":
        break


for i in range(10):
    if i == 5:
        break
    print(i)


nums = [3, 8, 2, 9, 1]
for n in nums:
    if n == 9:
        print("Found 9!")
        break


nums = [1, 3, 5, 6, 7]
for n in nums:
    if n % 2 == 0:
        print("First even:", n)
        break


for ch in "python":
    if ch == "h":
        break
    print(ch)
