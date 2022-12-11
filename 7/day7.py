#!/usr/bin/python

import re


def main():
    with open('input.txt') as inputfile:
        metadictionary = {}
        directories = []
        location = ''
        for i, line in enumerate(inputfile):
            line = line.replace('\n', '')
            if line.startswith('$ cd'):
                newDir = line.split(' ')[-1]
                if directories:
                    path = f'{location}/{newDir}' if location != '/' else f'/{newDir}'
                else:
                    path = newDir
                fullpath = re.sub(
                    r'/[a-z]+/\.\.', '', path, re.IGNORECASE
                )
                location = fullpath
                if fullpath in metadictionary:
                    continue
                directoryDict = {
                    'path': fullpath,
                    'size': 0,
                }
                directories.append(directoryDict)
                metadictionary[fullpath] = len(directories) - 1
            elif line.startswith('$') or line.startswith('dir'):
                continue
            else:
                filesize = int(line.split(' ')[0])
                directories[metadictionary[location]]['size'] += filesize
                parentdirs = ['/'] + directories[-1]['path'].split('/')[1:-1]
                if location != '/':
                    for j in range(len(parentdirs)):  # :/
                        parentpath = '/'+'/'.join(parentdirs[1:j+1])
                        directories[metadictionary[parentpath]]['size'] += filesize

    candidateDirsTotalSize = 0
    for directory in directories:
        if directory['size'] <= 100000:
            candidateDirsTotalSize += directory['size']
    print(f'Part1: {candidateDirsTotalSize}')

    freeSpace = 70000000 - directories[metadictionary['/']]['size']
    neededSpace = 30000000 - freeSpace
    chosen = directories[metadictionary['/']]
    for directory in directories:
        if directory['size'] < neededSpace:
            continue
        elif directory['size'] < chosen['size']:
            chosen = directory
    print(f"Part 2: {chosen['size']}")


if __name__ == '__main__':
    main()
