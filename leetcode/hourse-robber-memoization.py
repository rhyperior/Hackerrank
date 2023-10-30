# Url : https://leetcode.com/problems/house-robber/description/?envType=list&envId=exashqlm

# Solution uses memoization, problem is of type Overlapping Subproblem.


def house_robber(array=None):
    memoize_dict = dict()
    first_overlap = rob_step(memoize_dict, array, 1)
    second_overlap = array[0] + rob_step(memoize_dict, array, 2)

    return max(first_overlap, second_overlap)


def rob_step(memoize_dict={}, array=None, start=0):
    if start in memoize_dict:
        return memoize_dict[start]
    elif start > (len(array) - 1):
        return 0
    elif start == (len(array) - 1):
        return array[start]

    first_overlap = rob_step(memoize_dict, array, start + 1)
    second_overlap = array[start] + rob_step(memoize_dict, array, start + 2)

    result = max(first_overlap, second_overlap)
    memoize_dict[start] = result
    return result


if __name__ == "__main__":
    house_array = [1, 2, 3, 1]
    house_array = [2, 7, 9, 3, 1]
    house_array = [4, 1, 2, 7, 5, 3, 1]
    print(house_robber(house_array))
