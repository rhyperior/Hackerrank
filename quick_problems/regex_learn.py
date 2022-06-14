import re

sentence = """
Start a sentence and type it to the end
123-432-235
877.453.123 hh
"""
sentence = """code camp"""
# sentence = """abcd"""

# pattern = re.compile(r'(\s+)(.*)(\s+)')
pattern = re.compile(r'')
# pattern = re.compile(r'.*')


# matches =  re.finditer(pattern, sentence)
matches =  pattern.finditer(sentence)
# matches =  re.findall(r'\w\w\w(?i)', sentence)

# print('--'+re.sub(pattern=r'[^(\s)]', repl='', string=sentence)+'---')

# print(sentence)
# print(matches)
for match in matches:
    print(match)

# print(matches)