#!/usr/bin/python

def fullycontains(range1, range2):
    min1, max1 = map(int, range1.split('-'))
    min2, max2 = map(int, range2.split('-'))
    if min1 >= min2 and max1 <= max2:
        return True
    elif min2 >= min1 and max2 <= max1:
        return True
    else:
        return False


def overlaps(range1, range2):
    min1, max1 = map(int, range1.split('-'))
    min2, max2 = map(int, range2.split('-'))
    firstset = set(range(min1, max1 + 1))
    secondset = set(range(min2, max2 + 1))
    return not firstset.isdisjoint(secondset)


def main():
    with open('input.txt') as inputfile:
        countcontains = 0
        countoverlaps = 0
        for line in inputfile:
            elf1, elf2 = line[:-1].split(',')
            if fullycontains(elf1, elf2):
                countcontains += 1
            if overlaps(elf1, elf2):
                countoverlaps += 1
        print(f'Part 1: {countcontains}')
        print(f'Part 2: {countoverlaps}')


if __name__ == '__main__':
    main()
