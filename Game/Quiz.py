true = ["T", "t", "True"]
false = ["F", "f", "False"]
correct = 0

name = input("What's your name?")

print("\nOK, " + name + ", let's get started. Remember, the following answers are only True or False.")

print("\n python was invented by Guido van Rossum")
choice = input(">>> ")
if choice in true:
    correct += 1
else:
    correct += 0

print("\n.Is Python named after a Snake?")
choice = input(">>> ")
if choice in false:
    correct += 1
else:
    correct += 0

print("\n Python require a compiler.")
choice = input(">>> ")
if choice in false:
    correct += 1
else:
    correct += 0

print("\nPython is named comes from a TV comedy series.")
choice = input(">>> ")
if choice in true:
    correct += 1
else:
    correct += 0

print("\nPython is one of Google's official programming languages.")
choice = input(">>> ")
if choice in true:
    correct += 1
else:
    correct += 0

print("\nPython isn't a simple language.")
choice = input(">>> ")
if choice in false:
    correct += 1
else:
    correct += 0

print ("\nYou're finished, " + name + ". You got", correct, "out of 6 correct.")