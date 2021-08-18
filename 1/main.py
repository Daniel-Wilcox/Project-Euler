# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9.
# The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.

def sum_multiples(n):
    mul_3 = print_multiples(n, 3)
    mul_5 = print_multiples(n, 5)

    mul_3_and_5 = mul_3 + list(set(mul_5) - set(mul_3))
    print(sum(mul_3_and_5))


def print_multiples(n, m):
    multiples = []
    for i in range(1, n):
        if i % m == 0:
            multiples.append(i)

    return multiples


sum_multiples(1000)
