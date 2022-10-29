from typing import List
import re
'''
sample input :
3
07895462130
919875641230
9195969878
'''

def wrapper(func):
    def inner(*args, **kwargs):
        phone_number_list = []
        for index in range(len(args[0])):
            # match = re.search(r'\d{10}$', args[0][index])
            # args[0][index] = match.group(0)
            args[0][index] = args[0][index][-10:]

        # res = func(*args, **kwargs)
        for i in range(len(args[0])):
            args[0][i] = '+91 ' + args[0][i][:5] + ' ' + args[0][i][5:]
        return func(*args, **kwargs)
    return inner


@wrapper
def  sort_phone(l : List[str]) -> List[int]:
    # l.sort()
    # return l
    print(*sorted(l), sep='\n')

def extract_phone_numbers(l : List[str]) -> List[str] :
    phone_number_list = []
    for phone_number in l:
        match = re.search(r'\d{10}$', phone_number)
        phone_number_list.append(match.group(0))
    return phone_number_list

if __name__=="__main__":
    l = [input() for _ in range(int(input()))]

    # l = extract_phone_numbers(l)
    res = sort_phone(l)
    # print(res)
    # extract_phone_numbers(1)