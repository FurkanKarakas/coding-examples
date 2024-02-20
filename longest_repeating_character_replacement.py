"""https://leetcode.com/problems/longest-repeating-character-replacement/description/

Using the sliding window technique, keep two pointers i and j.

* If the total count minus the most frequent character gets more than k, we need to shift our left pointer
until the condition becomes true again.
* Total number of characters: j-i+1
* Update the result at each iteration after doing the modifications.
* There is a trick to this problem: we don't need to update (decrease) the most frequent character as we shift the left pointer.
We can keep it as it is (we are overestimating the value of the most frequent character, that's fine).
"""


from collections import defaultdict


def characterReplacement(s: str, k: int) -> int:
    char_count_dict = defaultdict(int)
    i = 0
    result = 0
    max_freq = 0
    for j in range(len(s)):
        char_count_dict[s[j]] += 1
        max_freq = max(max_freq, char_count_dict[s[j]])
        # Move i until it's true
        while j-i+1-max_freq > k:
            char_count_dict[s[i]] -= 1
            i += 1
        result = max(result, j-i+1)
    return result


if __name__ == "__main__":
    print(characterReplacement(s="ABAB", k=2))
