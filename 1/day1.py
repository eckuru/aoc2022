#!/usr/bin/python
import numpy as np


def main(path):
    with open('input.txt') as fin:
        personalSum = 0
        sums = []
        for line in fin:
            if line == '\n':
                sums.append(personalSum)
                personalSum = 0
            else:
                personalSum += int(line)
        result1 = np.max(sums)
        print(f'Part 1: {result1}')

        sortedsums = sorted(sums)
        result2 = sum(sortedsums[-3:])
        print(f'Part 2: {result2}')


if __name__ == '__main__':
    main('input.txt')
