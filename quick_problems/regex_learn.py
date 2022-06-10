import re

sentence = """
Start a sentence and type it to the end
123-432-235
877.453.123 hh
"""
sentence = """42 42"""


# pattern = re.compile(r'james(?i)')
pattern = re.compile(r'(\d{2})\s(\d{2})')

# matches =  re.finditer(pattern, sentence)
matches =  pattern.finditer(sentence)
# matches =  re.findall(r'\w\w\w(?i)', sentence)

# print(matches)
for match in matches:
    print(match)

# print(matches)