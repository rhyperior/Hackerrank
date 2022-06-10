"""
input()
In Python 2, the expression input() is equivalent to eval(raw _input(prompt)).

Code

>>> input()  
1+2
3
>>> company = 'HackerRank'
>>> website = 'www.hackerrank.com'
>>> input()
'The company name: '+company+' and website: '+website
'The company name: HackerRank and website: www.hackerrank.com'
Task

You are given a polynomial  of a single indeterminate (or variable), .
You are also given the values of  and . Your task is to verify if .

Constraints
All coefficients of polynomial  are integers.
 and  are also integers.

Input Format

The first line contains the space separated values of  and .
The second line contains the polynomial .

Output Format

Print True if . Otherwise, print False.

Sample Input

1 4
x**3 + x**2 + x + 1
Sample Output

True

1 -1
5*x**4 - 3*x**3 + 2*x**2 - 5

False

Hence, the output is True.
"""
import re

def calc(expression_list, X, Y):
    if expression_list:
        total_sum = 0
        for term in expression_list:
            sum = 1
            if term[0]=='-':
                sum = -1*sum
            sum = sum * term[1] * pow(X, term[2])
            total_sum = total_sum + sum

        if total_sum == Y:
            return True
        else: return False
    
    else :
        return '@No-Param'
if __name__=="__main__":
    # input = raw_input()
    X, Y = map(int, raw_input().split())
    input = raw_input()
    if input[0]!= '-':
        input = '+ ' + input

    # pattern = re.compile(r'([+-]\s\d[*]x[*]{2}){0,1}\d')
    pattern = re.compile(r'[+-]\s(\d[*]){0,1}(x[*]{2}){0,1}\d|([+-]\sx\b)')
    all_match = pattern.finditer(input)

    expression_list = []   #(sign, coefficient, power)

    pattern_2 = re.compile(r'[+-]|(\s\d)|([*]{2}\d)|x\b')
    for match in all_match:
        sign, coefficinet, power = '+', 1, 0
        exp = match.group()
        match_exp = pattern_2.finditer(exp)
        for match_op in match_exp:
            match_op = match_op.group()

            if match_op == '+' or match_op == '-':
                sign = match_op
            elif match_op[:2] == '**':
                power = int(match_op[2:])
            elif match_op[0] == ' ':
                coefficinet = int(match_op.strip())
            elif match_op[-1] == 'x':
                power = 1
            
        expression_list.append((sign, coefficinet, power))
    value = calc(expression_list=expression_list, X=X, Y=Y)
    print value