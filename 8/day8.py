#!/usr/bin/python
from numpy import loadtxt, vstack, argmin


def main():
    data = vstack(loadtxt('input.txt', dtype=int))
    treecount = 0
    mostscenic = 0
    for a in range(len(data[1:-1, 0])):
        for b in range(len(data[0, 1:-1])):
            i = a + 1
            j = b + 1
            height = data[i, j]
            if (
                    all(height > data[:i, j]) or
                    all(height > data[i, :j]) or
                    all(height > data[i+1:, j]) or
                    all(height > data[i, j+1:])
            ):
                treecount += 1
            scenicscore = 1
            scenicscore *= argmin(height > data[i-1::-1, j]) + 1 if not all(
                height > data[i-1::-1, j]) else len(data[i-1::-1, j])
            scenicscore *= argmin(height > data[i, j-1::-1]) + 1 if not all(
                height > data[i, j-1::-1]) else len(data[i, j-1::-1])
            scenicscore *= argmin(height > data[i+1:, j]) + 1 if not all(
                height > data[i+1:, j]) else len(data[i+1:, j])
            scenicscore *= argmin(height > data[i, j+1:]) + 1 if not all(
                height > data[i, j+1:]) else len(data[i, j+1:])
            if scenicscore > mostscenic:
                mostscenic = scenicscore

    print(f'Part 1: {treecount}')
    print(f'Part 2: {mostscenic}')


if __name__ == '__main__':
    main()
