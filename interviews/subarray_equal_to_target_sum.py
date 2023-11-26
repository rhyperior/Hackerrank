# Find Subarray with given sum

# Input: arr[] = {1, 4, 20, 3, 10, 5}, sum = 33
# Output: Sum found between indexes 2 and 4

# Input: arr[] = {1, 4, 0, 0, 3, 10, 5}, sum = 7
# Output: Sum found between indexes 1 and 4

# Input: arr[] = {1, 4}, sum = 0
# Output: No subarray found


def find_indexes(array, target):
    start_index = 0
    end_index = -1
    sum = 0

    # for i in range(len(array)):
    while True:
        if sum == target:
            if target == 0:
                if array[end_index] != 0:
                    end_index += 1
                    sum += array[end_index]
                    continue
            return [start_index, end_index]
        elif sum > target:
            sum -= array[start_index]
            start_index += 1

        elif sum < target:
            end_index += 1

            if end_index == len(array):
                return "no solution"

            sum += array[end_index]

    return "No subarray found"


print(find_indexes(array=[1, 4, 20, 3, 10, 5], target=33))  # [2,4]
print(find_indexes(array=[1, 4, 20, 3, 10, 5], target=30))  # No solution
print(find_indexes(array=[1, 4, 0, 0, 3, 10, 5], target=0))  # [2,3], [2,2]
print(find_indexes(array=[1, 4, 0, 0, 3, 10, 5], target=4))  # [2,3], [2,2]
print(find_indexes(array=[1, 4], target=5))  # [0,1]
print(find_indexes(array=[1, 4], target=4))  # [1,1]


# Product , price, -> 500, 700


# # Product.objects.filter(price.greaterthan)

# product_ids  = [4,5,2,3,1]

# Product.objects.filter(id=4)
