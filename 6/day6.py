#!/usr/bin/python

def main():
    with open('input.txt') as inputfile:
        signal = inputfile.readline()

    def n_unique(n, signal):
        block = signal[:n]
        for i, char in enumerate(signal[n:]):
            if len(set(block)) == n:
                return i + n
            else:
                block = block[1:] + char
    return n_unique(4, signal), n_unique(14, signal)


if __name__ == '__main__':
    part1, part2 = main()
    print(f'Part 1: {part1}')
    print(f'Part 2: {part2}')
