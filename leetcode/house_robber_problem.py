# Url : https://leetcode.com/problems/house-robber/description/?envType=list&envId=exashqlm

# This is an example of overlapping subproblem.


def house_robber(array=None):
    mid_point = (len(array) - 1) // 2

    first_overlap = rob_step(array, 0, mid_point - 1) + rob_step(
        array, mid_point + 1, len(array) - 1
    )
    second_overlap = rob_step(array, 0, mid_point) + rob_step(
        array, mid_point + 2, len(array) - 1
    )

    return max(first_overlap, second_overlap)


def rob_step(array, start, end):
    if start > end:
        return 0
    elif end - start == 1:
        return max(array[end], array[start])
    elif end == start:
        return array[start]

    mid_point = (end + start) // 2

    first_overlap = rob_step(array, start, mid_point - 1) + rob_step(
        array, mid_point + 1, end
    )
    second_overlap = rob_step(array, start, mid_point) + rob_step(
        array, mid_point + 2, end
    )

    return max(first_overlap, second_overlap)


if __name__ == "__main__":
    house_array = [1, 2, 3, 1]
    house_array = [2, 7, 9, 3, 1]
    house_array = [4, 1, 2, 7, 5, 3, 1]
    print(house_robber(house_array))
