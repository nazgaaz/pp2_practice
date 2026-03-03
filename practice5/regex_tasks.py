import re


def task_1():
    # 1) 'a' followed by zero or more 'b'
    pattern = r"^ab*$"
    tests = ["a", "ab", "abb", "abbb", "ac", "ba"]
    print("\nTask 1:", pattern)
    for s in tests:
        print(f"{s:<6} -> {bool(re.match(pattern, s))}")


def task_2():
    # 2) 'a' followed by two to three 'b'
    pattern = r"^ab{2,3}$"
    tests = ["abb", "abbb", "abbbb", "ab", "a", "b"]
    print("\nTask 2:", pattern)
    for s in tests:
        print(f"{s:<6} -> {bool(re.match(pattern, s))}")


def task_3():
    # 3) lowercase letters joined with underscore
    pattern = r"^[a-z]+_[a-z]+$"
    tests = ["hello_world", "test_case", "Hello_world", "helloWorld", "_abc", "abc_"]
    print("\nTask 3:", pattern)
    for s in tests:
        print(f"{s:<12} -> {bool(re.match(pattern, s))}")


def task_4():
    # 4) one uppercase letter followed by lowercase letters
    pattern = r"^[A-Z][a-z]+$"
    tests = ["London", "Paris", "london", "LONDON", "A", "Abc"]
    print("\nTask 4:", pattern)
    for s in tests:
        print(f"{s:<8} -> {bool(re.match(pattern, s))}")


def task_5():
    # 5) 'a' followed by anything, ending in 'b'
    pattern = r"^a.*b$"
    tests = ["ab", "axxb", "a123b", "abc", "ba", "a----b"]
    print("\nTask 5:", pattern)
    for s in tests:
        print(f"{s:<8} -> {bool(re.match(pattern, s))}")


def task_6():
    # 6) replace space, comma, dot with colon
    text = "Hello, world. Python is cool"
    result = re.sub(r"[ ,\.]", ":", text)
    print("\nTask 6: replace [ ,.] -> ':'")
    print("Original:", text)
    print("Result:  ", result)


def task_7():
    # 7) snake_case -> camelCase
    text = "hello_world_test"
    result = re.sub(r"_([a-z])", lambda m: m.group(1).upper(), text)
    print("\nTask 7: snake_case -> camelCase")
    print("Original:", text)
    print("Result:  ", result)


def task_8():
    # 8) split a string at uppercase letters (find words)
    text = "HelloWorldPython"
    parts = re.findall(r"[A-Z][a-z]*", text)
    print("\nTask 8: split at uppercase letters")
    print("Original:", text)
    print("Result:  ", parts)


def task_9():
    # 9) insert spaces between words starting with capital letters
    text = "HelloWorldPython"
    result = re.sub(r"([A-Z])", r" \1", text).strip()
    print("\nTask 9: insert spaces before capitals")
    print("Original:", text)
    print("Result:  ", result)


def task_10():
    # 10) camelCase -> snake_case
    text = "helloWorldPython"
    result = re.sub(r"([A-Z])", r"_\1", text).lower()
    print("\nTask 10: camelCase -> snake_case")
    print("Original:", text)
    print("Result:  ", result)


def main():
    task_1()
    task_2()
    task_3()
    task_4()
    task_5()
    task_6()
    task_7()
    task_8()
    task_9()
    task_10()


if __name__ == "__main__":
    main()