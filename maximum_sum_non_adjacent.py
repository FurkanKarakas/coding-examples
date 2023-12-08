"""Given an array of numbers, return an array of 0-1 (meaning if the item at index i is included) 
and the maximum sum such that no two adjacent elements are present in the result.

Let msna(m) be the maximum sum you can obtain until the element at index m inclusive. Then:

msna(m) = max(msna(m-2)+arr[m], msna(m-1))
"""


def maximum_sum_non_adjacent(arr: list[int]) -> tuple[list[int], int]:
    result_indices = [0]*len(arr)
    index_tracker = [0]*len(arr)

    msna = [0]*len(arr)

    for i in range(len(arr)):
        if i-2 < 0:
            msna_m_2 = 0
        else:
            msna_m_2 = msna[i-2]
        if i-1 < 0:
            msna_m_1 = 0
        else:
            msna_m_1 = msna[i-1]

        msna[i] = max(msna_m_2+arr[i], msna_m_1)
        # Keep track of the result
        if msna_m_2+arr[i] > msna_m_1:
            index_tracker[i] = i-2
        else:
            index_tracker[i] = i-1

    # Build the result
    i = len(arr)-1
    while i >= 0:
        if index_tracker[i] == i-2:
            result_indices[i] = 1
            i -= 2
        else:
            i -= 1

    return result_indices, msna[-1]


if __name__ == "__main__":
    arr_ = [5, 5, 10, 100, 10, 5]
    result_indices_, result = maximum_sum_non_adjacent(arr_)
    print(f"Result indices: {result_indices_}\nMaximum sum: {result}")
