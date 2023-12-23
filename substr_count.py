# https://www.hackerrank.com/challenges/special-palindrome-again/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=strings


"""A string is said to be a special string if either of two conditions is met:

- All of the characters are the same, e.g. aaa.
- All characters except the middle one are the same, e.g. aadaa.
A special substring is any substring of a string which meets one of those criteria. Given a string, determine how many special substrings can be formed from it.
"""


def substrCount(s):
    result = 0
    currentChr = s[0]
    count = 1
    charTuples = list()
    for char in s[1:]:
        if char == currentChr:
            count += 1
        else:
            charTuples.append((currentChr, count))
            currentChr = char
            count = 1
    charTuples.append((currentChr, count))
    nCharTuples = len(charTuples)
    # Get the individual characters
    for char, count in charTuples:
        result += count*(count+1)//2
    # Consider the middle elements
    for i, (char, count) in enumerate(charTuples):
        # A candidate for middle element (size: 1)
        # and the index must be in the list's reach (left tuple and right tuple)
        if count == 1 and i-1 >= 0 and i+1 <= nCharTuples-1:
            # Characters must match
            if charTuples[i-1][0] == charTuples[i+1][0]:
                # Get the minimum between two: e.g. ...aabaaa... -> get min(2,3) = 2
                result += min(charTuples[i-1][1], charTuples[i+1][1])
    return result


if __name__ == "__main__":
    sList = ["aaabbbcccdddeee", "abcdef", "abcbaba"]
    for s in sList:
        result = substrCount(s)
        print(f"There are {result} special substrings in '{s}'.")
