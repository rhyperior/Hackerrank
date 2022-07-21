import sys

if __name__=="__main__":
    a = [ 'a', 'b', 'c']
    b = [ 'b', 'c', 'd']
    c = list(set(a) - set(b))
    print(c)