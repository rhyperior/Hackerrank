import operator

"""
sample input 
3
Mike Thomson 20 M
Robert Bustle 32 M
Andria Bustle 30 F


failed input test case:
10
Jake Jake 42 M
Jake Kevin 57 M
Jake Michael 91 M
Kevin Jake 2 M
Kevin Kevin 44 M
Kevin Michael 100 M
Michael Jake 4 M
Michael Kevin 36 M
Michael Michael 15 M
Micheal Micheal 6 M


failed output respective:
Mr. Kevin Jake
Mr. Michael Jake
Mr. Micheal Micheal
Mr. Michael Michael
Mr. Michael Kevin
Mr. Jake Jake
Mr. Kevin Kevin
Mr. Jake Kevin
Mr. Jake Michael
Mr. Kevin Michael
"""

def person_lister(f):
    def inner(*args, **kwargs):
        args[0].sort(key=lambda x: int(operator.itemgetter(2)(x)))
        res = []
        for i in range(len(args[0])):
            res.append(f(args[0][i]))
        return res
    return inner


@person_lister
def name_format(person):
    return ('Mr. ' if person[3]=='M' else 'Ms. ') + person[0] + ' ' + person[1]

if __name__=="__main__":
    people = [input().split() for _ in range(int(input()))]
    
    print(*name_format(people), sep='\n')
    # res = []
    # for i in people:
    #     a = name_format(i)
    #     res.append(a)
