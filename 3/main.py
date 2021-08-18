# The prime factors of 13195 are 5, 7, 13 and 29.

# What is the largest prime factor of the number 600851475143 ?


def largest_prime_factor(n):
    largest_prime = 1
    m = n
    divider = 2

    while m > 1:
        if m % divider == 0:
            m = m / divider

            if divider > largest_prime:
                largest_prime = divider

        else:
            divider += 1

    return largest_prime


print(largest_prime_factor(600851475143))
