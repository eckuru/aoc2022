#!/usr/bin/python

def intersect3(setlist):
    set1, set2, set3 = setlist
    return set1.intersection(set2).intersection(set3).pop()


def main():
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    priorities = {
        letter: i + 1 for (i, letter) in enumerate(alphabet)
    }

    def priority(letter):
        if letter.islower():
            return priorities[letter]
        else:
            return priorities[letter.lower()] + 26

    with open('input.txt') as inputfile:
        result = 0
        groups = []
        group = []
        for i, line in enumerate(inputfile):
            stuff = line[:-1]
            stuffsize = int(len(stuff) / 2)
            letters = (set(stuff[:stuffsize]), set(stuff[stuffsize:]))
            commonletter = letters[0].intersection(letters[1]).pop()
            result += priority(commonletter)
            group.append(set(line[:-1]))
            if (i + 1) % 3 == 0:
                groups.append(group)
                group = []

        print(f'Part one: {result}')
        badges = [priority(intersect3(g)) for g in groups]

        print(f'Part two: {sum(badges)}')


if __name__ == '__main__':
    main()
