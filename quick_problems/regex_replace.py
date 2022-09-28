"""
The re.sub() tool (sub stands for substitution) evaluates a pattern and, for each valid match, it calls a method (or lambda).
The method is called for all matches and can be used to modify strings in different ways.
The re.sub() method returns the modified string as an output.

Learn more about .

Transformation of Strings

Code

import re

#Squaring numbers
def square(match):
    number = int(match.group(0))
    return str(number**2)

print re.sub(r"\d+", square, "1 2 3 4 5 6 7 8 9")
Output

1 4 9 16 25 36 49 64 81

Replacements in Strings

Code

import re

html = 
<head>
<title>HTML</title>
</head>
<object type="application/x-flash" 
  data="your-file.swf" 
  width="0" height="0">
  <!-- <param name="movie"  value="your-file.swf" /> -->
  <param name="quality" value="high"/>
</object>

print re.sub("(<!--.*?-->)", "", html) #remove comment
Output

<head>
<title>HTML</title>
</head>
<object type="application/x-flash" 
  data="your-file.swf" 
  width="0" height="0">

  <param name="quality" value="high"/>
</object>
Task

You are given a text of  lines. The text contains && and || symbols.
Your task is to modify those symbols to the following:

&& → and
|| → or
Both && and || should have a space " " on both sides.

Input Format

The first line contains the integer, .
The next  lines each contain a line of the text.

Constraints


Neither && nor || occur in the start or end of each line.

Output Format

Output the modified text.

Sample Input

11
a = 1;
b = input();

if a + b > 0 && a - b < 0:
    start()
elif a*b > 10 || a/b < 1:
    stop()
print set(list(a)) | set(list(b)) 
#Note do not change &&& or ||| or & or |
#Only change those '&&' which have space on both sides.
#Only change those '|| which have space on both sides.
Sample Output

a = 1;
b = input();

if a + b > 0 and a - b < 0:
    start()
elif a*b > 10 or a/b < 1:
    stop()
print set(list(a)) | set(list(b)) 
#Note do not change &&& or ||| or & or |
#Only change those '&&' which have space on both sides.
#Only change those '|| which have space on both sides.   
"""

import re

def reg_replace(match):
    if re.search(r'\s[&]{2}', match[0]) is not None:
        return ' and'
    elif re.search(r'\s[|]{2}', match[0]) is not None:
        return ' or'
    else :
        return ''

if __name__=="__main__":
    # N = int(input())

    # for _ in range(N):
    # text = input()
    text = ''
    while(True):
        try:
            line = input()
        except EOFError:
            break
        text = text + '\n'+ line

    matches = re.findall(r'\s[&]{2}(?=\s)|\s[|]{2}(?=\s)', text)
    print(matches)
    text2 = re.sub(r'\s[&]{2}(?=\s)|\s[|]{2}(?=\s)', reg_replace, text)
    print('---'*15)
    print(text2)
    # with open('./quick_problems/answer_regex_replace.txt', 'w+') as f:
    #     f.write(text2)