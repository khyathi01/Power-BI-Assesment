import os
with open('sample.txt','w') as file:
    file.write("hello people\n")

with open("sample.txt", "a") as file:
    file.write("completing the task assigned.\n")

with open("sample.txt", "r") as file:
    content = file.read()
    print(content)


if os.path.exists("newfile.txt"):
    print("newfile.txt exists")
