"""I want to implement some common bit operations in this file.
"""


class CommonBitOperations:
    def __init__(self) -> None:
        pass

    def isSet(self, num: int, pos: int) -> bool:
        """This method will return True if the bit at the given position is set.
        """
        return (num & (1 << pos)) != 0

    def setBit(self, num: int, pos: int) -> int:
        """This method will set the bit at the given position.
        To set a bit, we use the bitwise OR operator.
        """
        return num | (1 << pos)

    def unsetBit(self, num: int, pos: int) -> int:
        """This method will unset the bit at the given position.
        To unset a bit, we use the bitwise AND operator with the complement of the bit.
        """
        return num & ~(1 << pos)

    def countSetBits(self, num: int) -> int:
        """This method will count the number of set bits in the given number.
        """
        count = 0
        while num:
            count += num & 1
            num >>= 1
        return count


if __name__ == "__main__":
    c = CommonBitOperations()
    # Binary 5: 101
    print(c.isSet(5, 2))  # True
    print(c.setBit(5, 1))  # 7
    print(c.unsetBit(5, 2))  # 1
    print(c.countSetBits(5))  # 2
