#!/usr/bin/python
import numpy as np


def main(n):
    directions = {
        'R': np.array([+1, 0]),
        'L': np.array([-1, 0]),
        'U': np.array([0, +1]),
        'D': np.array([0, -1]),
    }
    with open('input.txt') as inputfile:
        visited = []
        ropepositions = [np.array([0, 0]) for i in range(n)]
        visited.append(tuple(ropepositions[-1]))
        for line in inputfile:
            line.replace('\n', '')
            direction, count = line.split(' ')
            for i in range(int(count)):
                ropepositions[0] += + directions[direction]
                for j in range(1, len(ropepositions)):
                    distance = ropepositions[j-1] - ropepositions[j]
                    if any(abs(distance) > 1):
                        if any(distance == 0):
                            ropepositions[j] += (distance / 2).astype(int)
                        else:
                            ropepositions[j] += np.sign(distance)
                if tuple(ropepositions[-1]) not in visited:
                    visited.append(tuple(ropepositions[-1]))

    return len(visited)


if __name__ == '__main__':
    part1 = main(2)
    part2 = main(10)
    print(f'Part 1: {part1}')
    print(f'Part 2: {part2}')
