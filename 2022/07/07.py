from dataclasses import dataclass
from typing import List, Dict, Tuple

input = open("07/07.txt").readlines()

example = [
    "$ cd /",
    "$ ls",
    "dir a",
    "14848514 b.txt",
    "8504156 c.dat",
    "dir d",
    "$ cd a",
    "$ ls",
    "dir e",
    "29116 f",
    "2557 g",
    "62596 h.lst",
    "$ cd e",
    "$ ls",
    "584 i",
    "$ cd ..",
    "$ cd ..",
    "$ cd d",
    "$ ls",
    "4060174 j",
    "8033020 d.log",
    "5626152 d.ext",
    "7214296 k",
    ]

@dataclass
class Item():
    name: str
    size: int

@dataclass
class File(Item):
    parent: Item

@dataclass
class Folder(Item):
    parent: Item
    children: Dict[str, Item]



def getSize(root: Folder) -> int:
    for c in root.children:
        if type(root.children[c]) == File:
            root.size += root.children[c].size
        else:
            root.size += getSize(root.children[c])
    return root.size

def analyseInput(input: List) -> Folder:
    # elements: Dict[str, File|Folder] = {'/': Folder('/', 0, '', [])}
    rootFolder = Folder('/', 0, None, {})
    currDir = rootFolder

    for i in input[1:]:
        i = i.strip()
        if i[:5] == '$ cd ':
            if i[5:] == '..':
                currDir = currDir.parent
            else:
                currDir = currDir.children[i[5:]]
            continue
        if i == '$ ls':
            continue
        t, name = i.split(" ")
        e = None
        if t == 'dir':
            e = Folder(name, 0, currDir, {})
        else:
            e = File(name, int(t), currDir)
        currDir.children[name] = e

    return rootFolder

def runPart1(root: Folder) -> int:
    part1 = 0
    if root.size < 100_000:
        part1 += root.size
    for c in root.children:
        if type(root.children[c]) == Folder:
            part1 += runPart1(root.children[c])
    return part1

def runPart2(root: Folder, neededSpace: int) -> List[Folder]|int:
    part2 = []
    if root.size > neededSpace:
        part2.append(root)
    for c in root.children:
        if type(root.children[c]) == Folder:
            part2 += runPart2(root.children[c], neededSpace)
    if root.name == '/':
        part2 = sorted(part2, key=lambda e: e.size)[0].size
    return part2

def puzzle(input):
    
    rootFolder = analyseInput(input)
    getSize(rootFolder)

    part1 = runPart1(rootFolder)

    neededSpace = rootFolder.size - 40_000_000
    part2 = runPart2(rootFolder, neededSpace)
    
    return (part1, part2)


try:
    assert(puzzle(example) == (95437, 24933642))
except AssertionError as e:
    print(f"Error in examples, got {puzzle(example)}")
    exit()

part1, part2 = puzzle(input)
print(f'{part1=}')
print(f'{part2=}')
print()