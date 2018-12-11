#!/usr/bin/env python
# -*- coding: utf-8 -*-

__mtime__ = '2018/12/1'


def compare(x, y):
    (min_v, max_v) = (x, y) if x < y else (y, x)

    if (max_v - min_v) < 0.000000001:
        return 0
    elif x > y:
        return 1
    else:
        return -1


def sqrt(x):
    float_x = float(x)

    if float_x == 1.0:
        sqrt_x = float_x
    else:
        (low, high) = (0.0, 1.0) if float_x < 1 else (1.0, float_x)
        sqrt_x = (low + high) / 2
        result = compare(sqrt_x * sqrt_x, float_x)
        while result != 0:
            if result == 1:
                high = sqrt_x
            else:
                low = sqrt_x

            sqrt_x = (low + high) / 2
            result = compare(sqrt_x * sqrt_x, float_x)
    return sqrt_x

if __name__ == "__main__":
    print sqrt(1)
    print sqrt(2)
    print sqrt(3)
    print sqrt(4)
    print sqrt(100)
    print sqrt(10000)
    print sqrt(0.01)

    def compute_pai(n=10000):
        import math
        return sum([math.sqrt((n + i + 1) * (n - i - 1)) for i in range(n)]) / n / n * 4

    print compute_pai(1000000)
