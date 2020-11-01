# https://www.hackerrank.com/challenges/sherlock-and-valid-string/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=strings&h_r=next-challenge&h_v=zen

"""Sherlock considers a string to be valid if all characters of the string appear the same number of times. It is also valid if he can remove just 1 character at 1 index in the string, and the remaining characters will occur the same number of times. Given a string , determine if it is valid. If so, return YES, otherwise return NO.
    """


def isValid(s):
    # Store the frequency of letters
    freqCount = dict()
    for char in s:
        freqCount[char] = freqCount.get(char, 0)+1
    # Store the number of occurrences of frequencies
    # E.g.: aabbc -> a:2, b:2, c:1 -> 2:2, 1:1
    valueCount = dict()
    for value in freqCount.values():
        valueCount[value] = valueCount.get(value, 0)+1
    if len(valueCount) < 2:
        return "YES"
    elif len(valueCount) > 2:
        return "NO"
    # Case where there are two elements
    first, second = list(valueCount.items())
    if first[1] == 1:
        # The difference between letter counts should be 1 or the letter count should be 1, so when we remove it, there are no letters of count 1 anymore.
        # Not absolute value since the order matters.
        if first[0]-second[0] == 1 or first[0] == 1:
            return "YES"
    elif second[1] == 1:
        # The same operations reversed
        if second[0]-first[0] == 1 or second[0] == 1:
            return "YES"
    return "NO"


if __name__ == "__main__":
    s = "aabbccd"
    result = isValid(s)
    print(f"Is the string {s} a valid string? The answer is: {result}")
