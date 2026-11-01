"""
We need to represent the integer n in binary format.

We initialize the result to 1. 
Starting with the most significant bit, we take the square of the result and if the current bit is 1, 
then we also multiply the result with x.

We make use of the following identity: x**a * x**b = x**(a+b)

Time complexity: O(log(n))
Space complexity: O(1)
"""


def fastExponentiation(x: float, n: int) -> float:
    if x == 0 and n <= 0:
        raise ArithmeticError("The arguments are invalid!")

    # Handle negative values
    if n < 0:
        x = 1/x

    n_temp = abs(n)
    num_digits = 0
    while n_temp > 0:
        n_temp >>= 1
        num_digits += 1

    n_temp = abs(n)
    res = 1
    for i in range(num_digits):
        n_temp >>= num_digits-1-i
        res **= 2
        # You can also check if it's odd by bitwise AND operatior: n_temp & 1
        if n_temp % 2 == 1:
            res *= x
        n_temp = abs(n)
    return res


if __name__ == "__main__":
    print(f"Pow(2,5): {fastExponentiation(2,5)}")
    print(f"Pow(2,0): {fastExponentiation(2,0)}")
    print(f"Pow(-2,5): {fastExponentiation(-2,5)}")
    print(f"Pow(-2,6): {fastExponentiation(-2,6)}")
    print(f"Pow(2,-1): {fastExponentiation(2,-1)}")
    print(f"Pow(0.2,-1): {fastExponentiation(0.2,-1)}")
    print(f"Pow(0.5,3): {fastExponentiation(0.5,3)}")
