import re

def func(inputString):
    wordToNumber_dict = {
        "zero": 0,
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9
    }
    
    numbers = []
    number = ''
    for item in inputString:
        # print(re.match(r'^(?![a-z])|\w+[^a-zA-Z]', item))
        if re.search('^(?![a-z])|\w+[^a-zA-Z]', item):          
            # print("Wrong Input")
            numbers.append("Wrong Input")
        else:
            result = re.findall(r'[A-Z][a-z]+|[a-z]+', item)
            # print(result)
            for _item in result:
                number += str(wordToNumber_dict.get(_item.lower(), 0))
            numbers.append(number)
            number = ""
    return numbers

def numbers_to_strings(argument):
    switcher = {
        0: "zero",
        1: "one",
        2: "two",
    }
    return switcher.get(argument, "nothing")

if __name__=="__main__":
    print(func(["oneFourTwoThree", "1twothree", "onetwothree", "eightEightEightNine"]))
    # print(func(["oneTwoThree"]))


    # print(numbers_to_strings(10))

# Expectedoutput: 123, wrong, wrong