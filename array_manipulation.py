# https://www.hackerrank.com/challenges/crush/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=arrays

"""Starting with a 1-indexed array of zeros and a list of operations, for each operation add a value to each of the array element between two given indices, inclusive. Once all operations have been performed, return the maximum value in the array."""


def array_manipulation(n, queries):
    myarray = [0]*(n+1)
    # Record the "slope" of the change rather than the change itself for a linear running time.
    for start, end, inc in queries:
        myarray[start-1] += inc
        myarray[end] -= inc
    mymax = myarray[0]
    cumsum = 0
    for i in myarray:
        cumsum += i
        if cumsum > mymax:
            mymax = cumsum
    return mymax


if __name__ == "__main__":
    queries = [[1, 5, 3], [4, 8, 7], [6, 9, 1]]
    n = 10
    max_sum = array_manipulation(n, queries)
    print(f"Maximum sum is {max_sum}.")
