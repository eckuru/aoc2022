#!/usr/bin/python

def part1():
    with open('input.txt') as inputfile:
        x = 1
        cycle = 1
        totalStrength = 0
        for line in inputfile:
            line = line.replace('\n', '')
            if line.startswith('noop'):
                cycle += 1
                if cycle in (20, 60, 100, 140, 180, 220):
                    totalStrength += cycle * x
            elif line.startswith('addx'):
                cycle += 1
                if cycle in (20, 60, 100, 140, 180, 220):
                    totalStrength += cycle * x
                x += int(line.split(' ')[-1])
                cycle += 1
                if cycle in (20, 60, 100, 140, 180, 220):
                    totalStrength += cycle * x
    print(f'Part 1: {totalStrength}')


def part2():
    def draw(cycle, x):
        if abs(x-(cycle % 40)) <= 1:
            return '#'
        else:
            return '.'

    def newline(crtline, cycle):
        if cycle % 40 == 0:
            print(''.join(crtline))
            return []
        else:
            return crtline

    with open('input.txt') as inputfile:
        x = 1
        cycle = 1
        crtLine = []
        for line in inputfile:
            line = line.replace('\n', '')
            if line.startswith('noop'):
                crtLine.append(draw(cycle, x))
                crtLine = newline(crtLine, cycle)
                cycle += 1
            elif line.startswith('addx'):
                crtLine.append(draw(cycle, x))
                crtLine = newline(crtLine, cycle)
                cycle += 1
                x += int(line.split(' ')[-1])
                crtLine.append(draw(cycle, x))
                crtLine = newline(crtLine, cycle)
                cycle += 1


if __name__ == '__main__':
    part1()
    part2()
