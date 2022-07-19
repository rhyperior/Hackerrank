import math


def binary_insort_search_recursive(arr, start, end, elem):
#   console.log(start, end, elem) ;
    print(start, end)
    if(end - start <= 1):
            if (arr[start] ==  elem):
                return start
            # }
            elif arr[end] == elem:
                return end
            # }
            elif elem < arr[start]:
                return start
            elif elem > arr[start] and elem < arr[end] :
                return end
            else :
                return end + 1
            
    # }

    else :
            if (arr[math.floor((end + start + 1)/2)] == elem) :
                    return math.floor((end + start + 1) /2) 
            # }
            elif(arr[math.floor((end + start + 1)/2)] > elem):
                return binary_insort_search_recursive(arr, start, math.floor((end + start +1 )/2), elem)
            
            else : 
                return binary_insort_search_recursive(arr, math.floor((end + start + 1)/2), end, elem)
            

    
if __name__=="__main__":
    print('abc')
    result = binary_insort_search_recursive([40, 41, 42, 44, 50], 0, 4, 40.5)
    print(result)

