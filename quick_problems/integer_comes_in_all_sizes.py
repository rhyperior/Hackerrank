"""
Integers in Python can be as big as the bytes in your machine's memory. There is no limit in size as there is:  (c++ int) or  (C++ long long int).

As we know, the result of  grows really fast with increasing .

Let's do some calculations on very large integers.

Task
Read four numbers, , , , and , and print the result of .

Input Format
Integers a, b, c and d are given on four separate lines, respectively.

Constraints

1 < a ,b ,c ,d < 1000


Output Format
Print the result of a^b + c^d on one line.
"""

if __name__=="__main__":
    # a = 1000
    # b = 1000
    # c = 7
    # d = 27
    # a,b, c, d = [int(x) for x in input().split()]
    # a, b, c ,d = map(int, input().split())
    a, b, c, d = int(input()), int(input()), int(input()), int(input())

    print(a**b+c**d)
