#!/usr/bin/python
import re


def main(part):
    # find positions of crates
    with open('input.txt') as inputfile:
        cratelines = []
        for line in inputfile:
            if '1' in line:
                positions = [
                    i for i, char in enumerate(line) if char.isdigit()
                ]
                break
            else:
                cratelines.append(line)

    bottomupCratelines = cratelines[-1::-1]
    # make crates
    crates = []
    for position in positions:
        crate = [
            line[position] for line in bottomupCratelines
            if line[position] != ' '
        ]
        crates.append(crate)

    # move stuff around
    movements = re.compile(r'move ([0-9]+) from ([0-9]+) to ([0-9]+)')
    with open('input.txt') as inputfile:
        if part == 1:
            for line in inputfile:
                if 'move' not in line:
                    continue
                amount, srcCrate, dstCrate = map(
                    int, movements.match(line).groups()
                )
                fromCrate = crates[srcCrate - 1]
                toCrate = crates[dstCrate - 1]
                for i in range(amount):
                    toCrate.append(fromCrate.pop())
        else:
            for line in inputfile:
                if 'move' not in line:
                    continue
                amount, srcCrate, dstCrate = map(
                    int, movements.match(line).groups()
                )
                toMove = crates[srcCrate - 1][-1*amount:]
                crates[srcCrate - 1] = crates[srcCrate - 1][:-1*amount]
                [crates[dstCrate - 1].append(thing) for thing in toMove]
    print(f'Part {part}')
    print(''.join([crate.pop() for crate in crates if crate]))


if __name__ == '__main__':
    main(1)
    main(2)
