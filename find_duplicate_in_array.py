"""Given an array of size n+1 containing integers from 1 to n, find the duplicate integer.

You must use O(1) auxiliary space.

This problem can be solved by a hashmap, but this requires O(n) space.
Instead, we will use Floyd's cycle detection algorithm using tortoise and hase.
Next index in our array will be the current number in the list.
Ex: elem1=nums[0] -> elem2=nums[elem1] -> elem3=nums[elem2] etc.
Each index elem_i is valid since 1 <= elem_i <= n.
Note that integers can't be 0. The first element should "escape" the index:

[0,1,2,3,4] : in this example, we are "stuck" at index 0 even though there are no duplicates.
"""


def find_duplicate(nums: list[int]):
    tortoise = hase = nums[0]

    while True:
        tortoise = nums[tortoise]
        hase = nums[nums[hase]]
        if hase == tortoise:
            hase = nums[0]
            while True:
                # If they are equal, this is our duplicate
                # It doesn't make sense to move pointers first now since they move at the same speed
                # 😎
                if hase == tortoise:
                    return tortoise
                tortoise = nums[tortoise]
                hase = nums[hase]


if __name__ == "__main__":
    nums_ = [1, 5, 2, 3, 4, 5, 6, 7, 9, 10]
    duplicate = find_duplicate(nums_)
    print(duplicate)
