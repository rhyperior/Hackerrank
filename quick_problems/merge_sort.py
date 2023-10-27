# input array = [23, 4, -2, 0, 18, 13, 7, 41, 87, 65, 77, 66, 57, -67, 21]
def merge_sort(array=None):
    sort(array, start=0, end=len(array) - 1)


def sort(array=None, start=0, end=0):
    if (end - start) <= 0:
        return
    first_half_end = start + (end - start) // 2
    second_half_start = start + (end - start) // 2 + 1
    sort(array, start=start, end=start + (end - start) // 2)  # Left Half
    sort(array, start=start + (end - start) // 2 + 1, end=end)  # Right Half
    merge_step(
        array, start, start + (end - start) // 2, start + (end - start) // 2 + 1, end
    )


def merge_step(array, start1=0, end1=0, start2=0, end2=0):
    aux_array = []
    i = start1
    j = start2
    while i <= end1 and j <= end2:
        if array[i] <= array[j]:
            aux_array.append(array[i])
            i += 1
        else:
            aux_array.append(array[j])
            j += 1

    if i > end1:
        aux_array.extend(array[j : end2 + 1])
    if j > end2:
        aux_array.extend(array[i : end1 + 1])

    start = min(start1, start2)
    end = max(end1, end2)

    array[start : end + 1] = aux_array
    del aux_array


if __name__ == "__main__":
    input = [23, 4, -2, 0, 18, 13, 7, 41, 87, 65, 77, 66, 57, -67, 21]
    merge_sort(array=input)
    print(input)
