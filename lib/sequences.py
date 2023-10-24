#!/usr/bin/env python3

def print_fibonacci(length):
    if not length:
        print([])
    elif length == 1:
        print([0])
    else:
        fib_list = [0, 1]
        for key in range(2, length):
            num = fib_list[key - 1] + fib_list[key - 2]
            fib_list.append(num)
        print(fib_list)