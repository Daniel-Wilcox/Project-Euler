# A palindromic number reads the same both ways.
# The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

# Find the largest palindrome made from the product of two 3-digit numbers.


# largest 3-digit number = 999
# smallest 3-digit number = 100


# def large_palindrome():
#     upper = 999
#     flag = 1

#     while flag == 1:
#         number = 999*upper
#         string = list(str(number))
#         half = int(len(string)/2)
#         left = string[0:half]

#         if len(string) % 2 == 0:
#             right = string[half:len(string)]
#             rev_right = right[::-1]

#         else:
#             left = string[0:half]
#             right = string[(half+1):len(string)]

#         if all([left == rev_right]):
#             flag = 0
#         else:
#             upper -= 1

#     return number


# def large_palindrome2():
#     upper = 999
#     flag = 1

#     while flag == 1:
#         number = 999*upper
#         string = list(str(number))
#         half = int(len(string)/2)
#         left = string[0:half]

#         if len(string) % 2 == 0:
#             right = string[half:len(string)]
#             rev_right = right[::-1]
#             if all([left == rev_right]):
#                 flag = 0
#             else:
#                 upper -= 1
#         else:
#             upper -= 1

#     return number


def brute_forced():
    biggest = 0
    combo = []
    for i in range(999, 99, -1):
        for j in range(999, 99, -1):
            number = i*j

            string = list(str(number))
            half = int(len(string)/2)
            left = string[0:half]

            if len(string) % 2 == 0:
                right = string[half:len(string)]

            else:
                left = string[0:half]
                right = string[(half+1):len(string)]

            rev_right = right[::-1]

            if all([left == rev_right]):

                if number > biggest:
                    biggest = number
                    combo = [i, j]

    return biggest, combo


print(brute_forced())
