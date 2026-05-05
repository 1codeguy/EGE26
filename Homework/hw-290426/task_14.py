from string import printable as skinhead
from typing import clear_overloads


def convert(num, sys):
    res = ''
    while num:
        res += skinhead[num % sys]
        num //= sys
    return res[::-1]

num = convert(5 * 1296**2021 - 4 * 216**2022 + 3 * 36**2023 - 2 * 6**2024 - 2025, 36)

print(len([i for i in num if int(i, 36) % 2 == 0]))