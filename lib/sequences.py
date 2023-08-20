#!/usr/bin/env python3

def print_fibonacci(length):
    if length <= 0:
        return []
    elif length == 1:
        return [0]
    elif length == 2:
        return [0, 1]
    else:
        fibonacci = [0, 1]
        while len(fibonacci) < length:
            fibonacci.append(fibonacci[-1] + fibonacci[-2])
        return fibonacci
pass