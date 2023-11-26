"""
Find the depth of normal words like "Hello", "hi" within the html text.
The html text can be assumed to be correct.
"""

import re

input_text = "<html><body><div><p>Hello</p><div><p>hi</p></div></div></body></html>"


def find_depth(input=None, word=None):
    _stack = []
    tags = re.findall(r"<.*?>|\w+", input)
    print(tags)

    for item in tags:
        if item[0] != "<":
            if item == word:
                return len(_stack)
            else:
                continue
        if _stack:
            if _stack[-1][1:] == item[2:]:
                _stack.pop()
            else:
                _stack.append(item)
        else:
            _stack.append(item)
    return -1


print(find_depth(input=input_text, word="Hello"))
print(find_depth(input=input_text, word="hi"))
print(find_depth(input=input_text, word="Hole"))
