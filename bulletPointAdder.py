#! /usr/bin/python3

import pyperclip


content = pyperclip.paste()
print(content)

lines = content.split("\n")

for i in range(len(lines)):
    lines[i] = "* " + lines[i]

content = "\n".join(lines)


#pyperclip.copy(content)
print(content)
