from ntpath import realpath
import os

def sixth_digit(N: int, numbers: list):
    print(f"N: {N} -- and list: {numbers}")
    sixDigit_ls = []
    for index in numbers:
        sum = 50
        
        while(sum>9):
            sum = 0
            for j in range(4,-1,-1):
                sum += int(index / (pow(10, j)))
                index = index % (pow(10, j))
                # print(f"Sum : {sum} -- index: {index}")
            
            index = sum

        sixDigit_ls.append(sum)       
    
    return sixDigit_ls

if __name__=="__main__":
    __location__ = os.path.realpath(
        os.path.join(os.getcwd(), os.path.dirname(__file__))
    )

    fptr = open(os.path.join(__location__, "input01.txt"), 'r')

    input =  fptr.read().rstrip().splitlines()

    N = int(input[0])

    numbers = []
    for number in input[1:]:
        numbers.append(int(number))
    # for i in range(0, N):
    #     numbers.append(int(input()))
    result = sixth_digit(N, numbers)
    print("--------------")
    print(result)
