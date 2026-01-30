
i = 1
while i < 6:
    print(i)
    if i == 3:
        break
    i += 1


nums = [4, 7, 9, 12]
i = 0
while i < len(nums):
    if nums[i] == 9:
        print("Found 9!")
        break
    i += 1


i = 0
while True:
    print("i =", i)
    i += 1
    if i == 5:
        break


while True:
    text = input("Type something (q to quit): ")
    if text == "q":
        break
    print("You typed:", text)


total = 0
i = 1
while i <= 10:
    total += i
    if total > 15:
        print("Limit reached:", total)
        break
    i += 1

