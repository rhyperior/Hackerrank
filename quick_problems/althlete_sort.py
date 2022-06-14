"""
You are given a spreadsheet that contains a list of  athletes and their details (such as age, height, weight and so on). You are required to sort the data based on the th attribute and print the final resulting table. Follow the example given below for better understanding.

image

Note that  is indexed from  to , where  is the number of attributes.

Note: If two attributes are the same for different rows, for example, if two atheletes are of the same age, print the row that appeared first in the input.

Input Format

The first line contains  and  separated by a space.
The next  lines each contain  elements.
The last line contains .

Constraints



Each element 

Output Format

Print the  lines of the sorted table. Each line should contain the space separated elements. Check the sample below for clarity.

Sample Input 0

5 3
10 2 5
7 1 0
9 9 9
1 23 12
6 5 9
1
Sample Output 0

7 1 0
10 2 5
6 5 9
9 9 9
1 23 12
Explanation 0

The details are sorted based on the second attribute, since  is zero-indexed.
"""
import pickle

def sort_atheletes(athlete_data:list, N, M, K):
    try:
        selected_attribute = []
        sorted_attribute = []
        position_list = []
        for item in athlete_data:
            selected_attribute.append(item[K])
        sorted_attribute = selected_attribute[:]
        sorted_attribute.sort()

        for item in sorted_attribute:
            pos = selected_attribute.index(item)
            position_list.append(pos)
        
        print("here")

        return position_list
    except Exception as e:
        print("error in sort_athletes fn:", str(e))
        return []
if __name__=="__main__":
    # nm = input().split()
    
    # N =  int(nm[0])
    # M =  int(nm[1])

    # athlete_attribute_list = []

    # for item in range(N):
    #     attributes = []
    #     attributes.extend(map(int, input().split()))
    #     athlete_attribute_list.append(attributes)
    
    # K = int(input())

    # with open('object_pickle.pkl', 'wb') as f:
    #     pickle.dump(athlete_attribute_list, f)
    with open('object_pickle.pkl', 'rb') as f:
        athlete_attribute_list = pickle.load(f)
  
    ex = sorted(athlete_attribute_list, key = lambda x:x[0])
    result_str = ' '.join(map(str, []))






    # "\n".join(   map  (lambda x: " ".join(  map(str, x)  ), sorted(athlete_attribute_list, key = lambda x: x[k])  )   )   

    # ex_1 = sorted(athlete_attribute_list, key = lambda x:x[1])
    # ex_2 = sorted(athlete_attribute_list, key = lambda x:x[2])


    # position_list = sort_atheletes(athlete_attribute_list, N, M, K)

    # for item in position_list:
    #     line_string = ''
    #     for i in athlete_attribute_list[item]:
    #         line_string = line_string + str(i) + ' '
    #     print(line_string.strip())

    print("input received")

