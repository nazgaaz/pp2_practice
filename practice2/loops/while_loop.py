
i = 1
while i < 6:
    print(i)
    i += 1


x = 0
while x <= 3:
    print("x =", x)
    x += 1


running = True
count = 0
while running:
    print("Loop:", count)
    count += 1
    if count == 3:
        running = False


password = ""
while password != "1234":
    password = input("Enter password: ")
print("Access granted")


fruits = ["apple", "banana", "cherry"]
while fruits:
    print("Removed:", fruits.pop())
